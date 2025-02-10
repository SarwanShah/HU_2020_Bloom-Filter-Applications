# Password and Plagiarism Detection Application Using Bloom Filters  

## **Project Overview**  
This project demonstrates the development of an application that performs both **password breach detection** and **plagiarism detection** using **Bloom Filters** and **hash functions**. It offers efficient, scalable solutions to check large datasets quickly without storing the entire data in memory.  

The application leverages **MurmurHash3**, **SHA1**, and custom **Bloom Filter** implementations, along with **Tkinter** for the graphical interface.

---

## **Features**  
- **Password Verification**:  
  Uses a Bloom Filter to verify if a password has been leaked or compromised.  

- **Plagiarism Detection**:  
  - Detects the percentage of text overlap between a user-provided document and a large corpus of pre-processed text.  
  - Uses a Bloom Filter to optimize large-scale text comparisons efficiently.  

- **Bloom Filter Implementation**:  
  - Supports customizable filter size and error probability.  
  - Efficient hashing using **MurmurHash3** and **SHA1**.  
  - Allows loading and saving filters to/from files.  

- **GUI Application**:  
  - Built with **Tkinter**.  
  - Provides interactive password verification.  
  - Displays the plagiarism detection percentage for documents.  

---

## **File Descriptions**  

- **Application.py**: Implements the main GUI application for password checking. Integrates filter loading and input handling.  
- **BloomFilter.py**: Defines the **Bloom Filter** class with methods for filter creation, loading, and item checking.  
- **filterFileHandler.py**: Provides helper functions to generate and manage Bloom Filters.  
- **Main.py**: Demonstrates both password and plagiarism detection workflows.  
- **MurmurHash3.py**: Implements the **MurmurHash3** hash function optimized for Bloom Filters.  

---

## **How It Works**  

### **Password Detection**  
1. **Data Preparation**: A dataset of hashed passwords is loaded into a Bloom Filter.  
2. **Verification**: The application checks if the input password is in the compromised dataset.  

### **Plagiarism Detection**  
1. **Filter Generation**: Text data (e.g., news articles) is processed to generate a Bloom Filter.  
2. **Document Comparison**: The user provides a document, and each line is checked against the Bloom Filter to determine the percentage of overlap.  
3. **Output**: The application outputs the plagiarism percentage.  
