
# **Screenshot Tools Suite**

A powerful collection of tools to automate screenshot capturing, process images, and compile them into organized PDF documents. This suite is ideal for anyone managing large numbers of screenshots or scanned images, offering tools that work both independently and together to streamline your workflow.

---

## **Why Use This Suite?**

### **Use Cases**
- **Automate Screenshot Capture**: Monitor changes on your screen and document them dynamically or capture screenshots manually with a hotkey.
- **Process Scanned Documents**: Split double-page scans into individual pages for better organization.
- **Create Professional PDFs**: Combine screenshots or scanned pages into a polished PDF document.

### **Who Is This For?**
- **Students**: Capture and organize study materials, lectures, or online classes efficiently.
- **Professionals**: Automate documentation for reports, dashboards, or presentations.
- **Researchers**: Document dynamic screen changes for experiments or data collection.
- **Content Creators**: Compile tutorials or guides from screenshots into structured documents.

---

## **Tools Overview**

This repository provides three key tools:

1. [**Screenshot Automator**](#1-screenshot-automator)
2. [**Screenshot Splitter Tool**](#2-screenshot-splitter-tool)
3. [**PDF Creator Tool**](#3-pdf-creator-tool)

---

### **1. Screenshot Automator**

**Description**  
The Screenshot Automator simplifies and automates the process of capturing screenshots. It supports both manual and automatic modes, allowing you to monitor changes in a specific area of your screen or capture on demand using a hotkey.

**Key Features**:
- **Area Selection**: Select a specific region of your screen to monitor or capture.
- **Two Modes**:
  - **Manual Mode**: Capture screenshots with a customizable hotkey (`Ctrl+Shift+K` by default).
  - **Automatic Mode**: Detect changes in the selected area and capture screenshots dynamically.
- **Feedback**: Includes a visual flash effect and an audio notification to indicate successful screenshot capture.
- **Output Management**: Saves screenshots in a user-specified folder with timestamps.

**How to Use**:
1. Run the script.
   
      ```bash
      python3 tr4m0tter.py
   ```
2. Use your mouse to select an area on the screen for capturing.
3. Choose a mode:
   - **Manual Mode**: Press the hotkey to take screenshots.
   - **Automatic Mode**: Let the script monitor the area and capture screenshots whenever changes are detected.
4. Screenshots are saved in the folder you specify.

**Example Use Case**:
- Monitor a live stock trading dashboard or a dynamic report and automatically capture screenshots when the data updates.

---

### **2. Screenshot Splitter Tool**

**Description**  
The Screenshot Splitter Tool is designed to split images (e.g., screenshots or scans) into two equal parts. This is particularly useful for processing double-page scans or multi-section screenshots.

**Key Features**:
- Splits images **vertically** into two equal sections.
- Supports common image formats such as PNG, JPG, and JPEG.
- Processes all images in a selected folder.
- Saves the split images in a new subfolder named `split`.

**How to Use**:
1. Run the script.

```bash
      python3 splitter.py
```
2. Select the folder containing the images you want to split.
3. The tool splits all images in the folder and saves the results in a `split` subfolder.

**Example Use Case**:
- You’ve scanned multiple double-page book spreads, and now you want to split them into individual pages for easier reading or sharing.

---

### **3. PDF Creator Tool**

**Description**  
The PDF Creator Tool combines multiple images into a single PDF document. It automatically sorts images by their filenames (e.g., `screenshot_1.png`, `screenshot_2.png`, etc.) to ensure they are in the correct order.

**Key Features**:
- Selects and processes images from a specified folder.
- Automatically sorts images **numerically** by filename to maintain proper order.
- Supports common image formats such as PNG, JPG, and JPEG.
- Handles transparency by converting images to PDF-compatible RGB mode.

**How to Use**:
1. Run the script.
```bash
      python3 pdf_converter.py
```
2. Select the folder containing the images to convert.
3. Choose a name and location for the output PDF.
4. The tool creates a PDF with the images in the correct order.

**Example Use Case**:
- Compile lecture slides, scanned notes, or tutorial screenshots into a single, organized PDF document.

---

## **Combining the Tools**

These tools are designed to work seamlessly together to create a complete screenshot management workflow:

1. **Capture Screenshots**: Use the **Screenshot Automator** to take screenshots either manually or automatically based on changes in a selected area.
2. **Process Screenshots**: Use the **Screenshot Splitter Tool** to divide combined images into individual sections or pages.
3. **Organize and Share**: Use the **PDF Creator Tool** to combine the processed images into a single PDF file.

### **Example Workflow**
1. Use the **Screenshot Automator** during a webinar to capture important slides or dynamic data updates.
2. If the screenshots are wide or contain multiple sections, process them with the **Screenshot Splitter Tool** to break them into smaller parts.
3. Compile all the processed images into a clean, professional PDF using the **PDF Creator Tool**.

---

## **Requirements**

- **Python 3.7+**
- Required Libraries:
  - `Pillow` (for image processing)
  - `keyboard` (for hotkey handling)
  - `tkinter` (for UI dialogs, included with Python)

### Installation
Install the required libraries using:
```bash
pip install pillow keyboard
```

---

## **How to Run**

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/screenshot-tools-suite.git
   cd screenshot-tools-suite
   ```

2. Run the desired script:
   - **Screenshot Automator**:
     ```bash
     python screenshot_automator.py
     ```
   - **Screenshot Splitter Tool**:
     ```bash
     python splitter_tool.py
     ```
   - **PDF Creator Tool**:
     ```bash
     python pdf_creator_tool.py
     ```

---

## **Limitations**
  - Ensure filenames are properly numbered (e.g., `screenshot_1.png`, `screenshot_2.png`) for the correct order in the PDF.
