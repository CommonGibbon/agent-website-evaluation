import json
import os
import argparse
from datetime import datetime

def format_action_list(actions):
    """Format the action list with proper indentation and visual separators"""
    formatted = []
    for i, action in enumerate(actions, 1):
        if action.startswith("[Action]:"):
            formatted.append(f"**[Action]:**{action.replace('[Action]:', '')}\n")
        elif action.startswith("[AI Thought]:"):
            formatted.append(f"**[AI Thought]:** {action.replace('[AI Thought]:', '')}\n")
        else:
            formatted.append(action)
    
    return "\n".join(formatted)

def format_feedback(feedback_list):
    """Format the feedback Q&A pairs with visual separators"""
    formatted = []
    for i, item in enumerate(feedback_list, 1):
        formatted.append(f"**Q{i}: {item['question']}**\n")
        formatted.append(f"**A{i}:** {item['answer']}\n")
        
    
    return "\n".join(formatted)

def format_prompt(prompt_text):
    """Format the prompt text with proper line breaks"""
    # Clean up the prompt text and preserve formatting
    lines = prompt_text.strip().split('\n')
    formatted_lines = []
    for line in lines:
        if line.strip():
            formatted_lines.append(line.strip())
        else:
            formatted_lines.append("")  # Preserve empty lines
    return "\n".join(formatted_lines)

def create_report(json_data, filename):
    """Create a formatted report from JSON data"""
    report = []
    
    # Header
    report.append(f"# User Experience Report")
    report.append(f"**Source:** {filename}")
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # Goal
    report.append("## 🎯 Goal")
    report.append(json_data.get('goal', 'No goal specified'))
    report.append("")
    
    # User Persona/Prompt
    report.append("## 👤 User Persona")
    report.append("```")
    report.append(format_prompt(json_data.get('prompt', '')))
    report.append("```")
    report.append("")
    
    # Action Sequence
    report.append("## 🔄 Action Sequence")
    report.append(format_action_list(json_data.get('action_list', [])))
    report.append("")
    
    # User Feedback
    report.append("## 💬 User Feedback")
    report.append(format_feedback(json_data.get('feedback', [])))
    report.append("")
    
    # Metrics
    report.append("## 📊 Performance Metrics")
    report.append(f"- **Total Time:** {json_data.get('total_time', 0):.2f} seconds")
    report.append(f"- **Total Steps:** {json_data.get('total_steps', 0)}")
    if json_data.get('total_steps', 0) > 0:
        avg_time = json_data.get('total_time', 0) / json_data.get('total_steps', 1)
        report.append(f"- **Average Time per Step:** {avg_time:.2f} seconds")
    report.append("")
    
    return "\n".join(report)

def process_json_files(directory_path, output_directory):
    """Process all JSON files in a directory and create reports"""
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    if not os.path.exists(directory_path):
        print(f"Error: Log directory '{directory_path}' does not exist.")
        return

    # Find all JSON files
    json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]
    
    if not json_files:
        print(f"No JSON files found in {directory_path}")
        return
    
    print(f"Found {len(json_files)} JSON files to process in {directory_path}...")
    
    for filename in json_files:
        input_path = os.path.join(directory_path, filename)
        
        try:
            # Read JSON file
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Create report
            report = create_report(data, filename)
            
            # Save report
            output_filename = filename.replace('.json', '_report.md')
            output_path = os.path.join(output_directory, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            
            print(f"✅ Created report: {output_filename}")
            
        except Exception as e:
            print(f"❌ Error processing {filename}: {str(e)}")
    
    print(f"\nAll reports saved to: {output_directory}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON logs to Markdown reports.")
    parser.add_argument("log_dir", help="Path to the directory containing JSON logs")
    
    args = parser.parse_args()
    
    # Determine project root and output directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "report_data")
    
    process_json_files(args.log_dir, output_dir)
