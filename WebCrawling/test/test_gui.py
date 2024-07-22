import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as message
class  asd:
    root = tk.Tk()
    root.geometry('1200x600')
    # 트리뷰 [ 2차원 배열을 표현하기 위한 개체 ]
    tree = ttk.Treeview(root,columns=('1','2','3','4'))
    
    tree.column('#0', minwidth=300 ,width=200)
    tree.column('1', minwidth=120 ,width=200)
    tree.column('2', minwidth=120 ,width=200)
    tree.column('3', minwidth=160 ,width=200)
    tree.column('4', minwidth=200 ,width=200)
    tree.heading('#0', text='종목')
    tree.heading('1', text='현재가')
    tree.heading('2', text='전일비')
    tree.heading('3', text='등락률(%)')
    tree.heading('4', text='거래량')
    
    
    data = [
        ("삼성전자", "82,000", "1,200", "1.49", "1,234,567"),
        ("LG화학", "715,000", "5,000", "-0.69", "345,678"),
        ("카카오", "122,000", "2,000", "1.67", "789,012"),
        ("네이버", "380,000", "3,000", "-0.78", "567,890")
    ]

    for item in data:
        current_price = item[1]
        change_amount = item[2]
        change_percent = float(item[3])

        if change_percent > 0:
            change_amount_with_symbol = f"▲ {change_amount}"
            tag = 'positive'
        elif change_percent < 0:
            change_amount_with_symbol = f"▼ {change_amount}"
            tag = 'negative'
        else:
            change_amount_with_symbol = change_amount
            tag = ''

        tree.insert('', 'end', text=item[0], values=(current_price, change_amount_with_symbol, item[3], item[4]), tags=(tag,))

    # 태그별 텍스트 색상 설정
    tree.tag_configure('negative', foreground='blue')
    tree.tag_configure('positive', foreground='red')
        
    scroll = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    scroll.grid(row=0, column=1, sticky="ns")
    tree.config(yscrollcommand=scroll.set)
   
    tree.grid(column=0, row=0, padx=20, pady=20)
    root.grid_columnconfigure(0, weight=1)
    
    
   
   
   
   
    root.mainloop()
asd()