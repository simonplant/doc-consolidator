# FILENAME: consolidate.py
import os
import json
import argparse
import google.generativeai as genai

# --- CONFIGURATION ---

# Configure the Gemini API key
# Make sure to set the GOOGLE_API_KEY environment variable in your terminal
# For example: export GOOGLE_API_KEY="YOUR_API_KEY"
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("ERROR: The GOOGLE_API_KEY environment variable is not set.")
    print("Please set it to your Google API key.")
    exit()

# --- HELPER FUNCTIONS ---

def load_text_file(filepath):
    """Loads a text file and returns its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def save_text_file(content, filepath):
    """Saves content to a text file."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully saved file to {filepath}")
    except Exception as e:
        print(f"Error saving file {filepath}: {e}")

def load_documents_from_input(input_dir):
    """Loads all .txt and .md documents from the input directory."""
    documents = []
    print(f"\nLoading documents from '{input_dir}'...")
    for filename in os.listdir(input_dir):
        if filename.endswith(('.txt', '.md')):
            filepath = os.path.join(input_dir, filename)
            content = load_text_file(filepath)
            if content:
                # In a real app, you'd get the real timestamp. Here we use a placeholder.
                doc = {
                    "doc_id": filename,
                    "file_name": filename,
                    "timestamp": "2024-01-01T12:00:00Z", # Placeholder timestamp
                    "text_content": content
                }
                documents.append(doc)
    print(f"Loaded {len(documents)} documents.")
    return documents

def call_gemini_api(prompt_text, model_name="gemini-1.5-flash"):
    """Calls the Gemini API with a given prompt."""
    print(f"\nCalling Gemini API with model {model_name}...")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt_text)
        print("API call successful.")
        return response.text
    except Exception as e:
        print(f"An error occurred during the API call: {e}")
        return None

def parse_multi_file_output(raw_output):
    """Parses the multi-file format from the final prompt's output."""
    files = {}
    # Use a unique delimiter that's unlikely to be in the content
    delimiter = "---[ FILENAME:"
    parts = raw_output.split(delimiter)
    
    for part in parts:
        if not part.strip():
            continue
        try:
            header, content = part.split(']---', 1)
            filename = header.strip()
            files[filename] = content.strip()
        except ValueError:
            print(f"Warning: Could not parse a file block:\n{part[:100]}...")
            
    return files


# --- MAIN ORCHESTRATION LOGIC ---

def main():
    """Main function to orchestrate the document consolidation process."""
    
    # 1. Argument Parsing
    parser = argparse.ArgumentParser(description="AI Document Consolidation System")
    parser.add_argument('--config', type=str, required=True, help='Path to the config.json file.')
    args = parser.parse_args()

    # 2. Load Configuration
    print("--- Document Consolidation System Initializing ---")
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
        print(f"Configuration loaded from {args.config}")
    except FileNotFoundError:
        print(f"Error: Config file not found at {args.config}")
        return
    
    # Define project directories
    project_root = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(project_root, 'input')
    output_dir = os.path.join(project_root, 'output')
    processing_dir = os.path.join(project_root, 'processing')
    prompts_dir = os.path.join(project_root, 'prompts')
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(processing_dir, exist_ok=True)
    
    # --- PROMPT EXECUTION CHAIN ---
    
    # Step 1: Analysis & Scoring (Prompt 1)
    print("\n--- Phase 1 of 5: Analysis & Scoring ---")
    prompt1_template = load_text_file(os.path.join(prompts_dir, '1_analysis_prompt.md'))
    documents = load_documents_from_input(input_dir)
    if not documents:
        print("No documents found in the input directory. Exiting.")
        return
        
    # Inject config and documents into the prompt template
    prompt1_filled = prompt1_template.replace('{ai_persona}', json.dumps(config['ai_persona']))
    prompt1_filled = prompt1_filled.replace('{processing_principles}', json.dumps(config['processing_principles']))
    prompt1_filled = prompt1_filled.replace('"[...documents...]"', json.dumps(documents, indent=2))
    
    analysis_json_str = call_gemini_api(prompt1_filled)
    if not analysis_json_str:
        print("Analysis failed. Exiting.")
        return
    
    # Clean the output to be valid JSON
    analysis_json_str = analysis_json_str.strip().replace('```json', '').replace('```', '')
    analysis_filepath = os.path.join(processing_dir, '1_analysis_results.json')
    save_text_file(analysis_json_str, analysis_filepath)

    # Step 2: Structure Proposal (Prompt 2)
    print("\n--- Phase 2 of 5: Structure Proposal ---")
    prompt2_template = load_text_file(os.path.join(prompts_dir, '2_structure_prompt.md'))
    prompt2_filled = prompt2_template.replace('{ai_persona}', json.dumps(config['ai_persona']))
    prompt2_filled = prompt2_filled.replace('"[...analysis_json...]"', analysis_json_str)

    proposed_toc_md = call_gemini_api(prompt2_filled)
    if not proposed_toc_md:
        print("Structure proposal failed. Exiting.")
        return
        
    proposed_toc_filepath = os.path.join(processing_dir, '2_proposed_toc.md')
    save_text_file(proposed_toc_md, proposed_toc_filepath)
    
    # Step 3: Human-in-the-Loop - Approve the TOC
    print("\n--- ACTION REQUIRED: Please review and approve the Table of Contents ---")
    print(f"The proposed structure has been saved to: {proposed_toc_filepath}")
    print("Please review this file. You can make edits if desired.")
    input("Press Enter to continue once you have approved the file...")
    
    # Load the (potentially edited) TOC for the next step
    approved_toc_md = load_text_file(proposed_toc_filepath)
    
    # Step 4: Content Synthesis (Prompt 3)
    print("\n--- Phase 3 of 5: Content Synthesis ---")
    prompt3_template = load_text_file(os.path.join(prompts_dir, '3_synthesis_prompt.md'))
    prompt3_filled = prompt3_template.replace('{ai_persona}', json.dumps(config['ai_persona']))
    prompt3_filled = prompt3_filled.replace('"[...approved_toc...]"', approved_toc_md)
    prompt3_filled = prompt3_filled.replace('"[...analysis_json...]"', analysis_json_str)
    
    synthesized_draft_md = call_gemini_api(prompt3_filled)
    draft_filepath = os.path.join(processing_dir, '3_synthesized_draft.md')
    save_text_file(synthesized_draft_md, draft_filepath)

    # Step 5: Final Editing (Prompt 4)
    print("\n--- Phase 4 of 5: Final Editing & QA ---")
    prompt4_template = load_text_file(os.path.join(prompts_dir, '4_editing_prompt.md'))
    prompt4_filled = prompt4_template.replace('{ai_persona}', json.dumps(config['ai_persona']))
    prompt4_filled = prompt4_filled.replace('"[...synthesized_draft...]"', synthesized_draft_md)
    
    final_document_md = call_gemini_api(prompt4_filled)
    final_doc_filepath = os.path.join(processing_dir, '4_final_document.md')
    save_text_file(final_document_md, final_doc_filepath)

    # Step 6: Final Output Generation (Prompt 5)
    print("\n--- Phase 5 of 5: Generating Final Output Package ---")
    prompt5_template = load_text_file(os.path.join(prompts_dir, '5_output_gen_prompt.md'))
    prompt5_filled = prompt5_template.replace('"[...final_document...]"', final_document_md)
    prompt5_filled = prompt5_filled.replace('"[...analysis_json...]"', analysis_json_str)
    
    final_package_raw = call_gemini_api(prompt5_filled)
    
    # Parse the multi-file output and save each file
    output_files = parse_multi_file_output(final_package_raw)
    for filename, content in output_files.items():
        # Make sure supplementary files go into their own subdirectory
        if filename.startswith('supplementary/'):
             filepath = os.path.join(output_dir, filename)
        else:
             filepath = os.path.join(output_dir, filename)
        save_text_file(content, filepath)

    print("\n--- Document Consolidation Process Complete! ---")
    print(f"All final files have been saved in the '{output_dir}' directory.")


if __name__ == '__main__':
    main()