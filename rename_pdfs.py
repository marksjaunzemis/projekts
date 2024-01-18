import os

def rename_pdfs(folder_path):
  pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

  if not pdf_files:
    print('nav pdf failu mapē')
    return

  for i, pdf_file in enumerate(pdf_files, start=1):
    old_path = os.path.join(folder_path, pdf_file)
    new_path = os.path.join(folder_path, f"{i}.pdf")

    os.rename(old_path, new_path)
    print(f"No '{pdf_file}' Uz '{i}.pdf'")

  print(f"tika pārsaukti {len(pdf_files)} pdf faili")

def main():
  folder_path = input("ievadi ceļu līdz mapei")

  try:
    rename_pdfs(folder_path)
  except Exception as e:
    print(f"kļūda")

if __name__ == "__main__":
  main()
