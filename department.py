names = [
  ("Mandipa Thapa","Engineering"),
  ("Anusha Thapa","MBBS"),
  ("Sunayana Thapa","IT"),
  ("Asmii Gurung","IT"),
  ("Ram KC","HM"),
  ("Arnabi Karki","LLB"),
  ("Nishant Thapa","IT"),
  ("Shivanshi Khatri","Engineering"),
  ("Shikha Thapa","MBBS"),
  ("Sampreson Thapa","IT")
]
IT_names = [name for name in names if name[1] == "IT" ]
print(IT_names)