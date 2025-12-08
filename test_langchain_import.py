try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
