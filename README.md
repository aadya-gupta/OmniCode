# OmniCode

## Overview
OmniCode is an intelligent coding assistant designed to enhance developer productivity. It provides a unified platform for code generation, bug detection, unit test creation, and code explanation. By integrating AI-powered solutions with static analyzers, OmniCode streamlines the software development process while supporting multiple programming languages.

## Features
- **Code Generation:** Generate clean, well-documented code from simple descriptions.  
- **Bug Detection:** Identify and fix bugs using static analysis and AI-generated insights.  
- **Unit Test Generation:** Quickly generate comprehensive unit tests for any code.  
- **Code Explanation:** Understand complex code through clear, beginner-friendly explanations.  
- **Multi-language Support:** Automatically detects and supports various programming languages.  
- **User-friendly Interface:** Sleek and colorful interface with a pastel and blue theme for an engaging user experience.  

## Technology Stack
- **Frontend:** Streamlit  
- **AI Model:** Gemini API  
- **Static Analyzers:**  
  - Python: Pylint  
  - JavaScript: ESLint  
  - Java: Checkstyle  
  - C++: CPPCheck  
  - Go: Golint  
- **Supported Languages:** Python, JavaScript, Java, C++, Go  

## Installation
### Prerequisites
- Python 3.8 or above  
- pip (Python package manager)

### Steps
1. Clone the repository:  
   ```bash
   git clone https://github.com/aadya-gupta/OmniCode
   cd OmniCode

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a .env file and add your Gemini API key:
   ```bash
   API_KEY=your_gemini_api_key

5. Run the application:
   ```bash
   streamlit run app.py

## Project Structure 
<img width="620" alt="Screenshot 2025-02-26 at 12 02 02 PM" src="https://github.com/user-attachments/assets/d858e1f4-83e5-4390-bd44-858c83a5f365" />

## Usage
- Code Generation: Enter a code description to generate relevant code.
-	Bug Detection: Paste code to identify bugs and receive corrections.
-	Unit Test Generation: Provide code to generate unit tests automatically.
-	Code Explanation: Paste code to receive clear explanations.

## Challenges and Solutions
- Static Analysis Integration: Mapped programming languages to appropriate analyzers for accurate bug detection.
- Language Detection: Implemented AI-driven language detection for seamless user experience.
- User Interface Design: Created a pastel-themed, intuitive interface for ease of use.

## Future Improvements
- Expand language support beyond current offerings.
- Implement real-time collaborative features.
- Enhance code optimization suggestions.
- Deploy as a hosted web application for broader accessibility.

## License
This project is for the Google Girl Hackathon 2025 and is intended for educational and demonstration purposes.
