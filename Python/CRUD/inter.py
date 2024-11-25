import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class AplicacaoCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        
        # Criar conexão com o banco de dados
        self.conn = sqlite3.connect('usuarios.db')
        self.criar_tabela()
        
        # Variáveis para armazenar os dados
        self.id = tk.StringVar()
        self.nome = tk.StringVar()
        self.email = tk.StringVar()
        self.telefone = tk.StringVar()
        
        # Frame para entrada de dados
        frame_dados = ttk.LabelFrame(root, text="Dados do Usuário", padding="10")
        frame_dados.grid(row=0, column=0, padx=10, pady=5)
        
        # Campos de entrada
        ttk.Label(frame_dados, text="ID:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame_dados, textvariable=self.id, state='readonly').grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Nome:").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame_dados, textvariable=self.nome).grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Email:").grid(row=2, column=0, sticky="w")
        ttk.Entry(frame_dados, textvariable=self.email).grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Telefone:").grid(row=3, column=0, sticky="w")
        ttk.Entry(frame_dados, textvariable=self.telefone).grid(row=3, column=1, padx=5, pady=2)
        
        # Frame para botões
        frame_botoes = ttk.Frame(root)
        frame_botoes.grid(row=1, column=0, pady=10)
        
        # Botões
        ttk.Button(frame_botoes, text="Adicionar", command=self.adicionar_registro).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botoes, text="Atualizar", command=self.atualizar_registro).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botoes, text="Deletar", command=self.deletar_registro).grid(row=0, column=2, padx=5)
        ttk.Button(frame_botoes, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)
        
        # Tabela
        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Telefone"), show="headings")
        self.tree.grid(row=2, column=0, padx=10, pady=5)
        
        # Cabeçalhos da tabela
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefone", text="Telefone")
        
        # Configurar largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Telefone", width=100)
        
        # Bind para selecionar item
        self.tree.bind('<<TreeviewSelect>>', self.selecionar_item)
        
        # Carregar dados
        self.carregar_dados()
    
    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT,
                telefone TEXT
            )
        """)
        self.conn.commit()
    
    def adicionar_registro(self):
        if not self.nome.get():
            messagebox.showerror("Erro", "Por favor, preencha o nome!")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nome, email, telefone)
                VALUES (?, ?, ?)
            """, (self.nome.get(), self.email.get(), self.telefone.get()))
            self.conn.commit()
            
            self.limpar_campos()
            self.carregar_dados()
            messagebox.showinfo("Sucesso", "Registro adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar registro: {str(e)}")
    
    def atualizar_registro(self):
        if not self.id.get():
            messagebox.showerror("Erro", "Por favor, selecione um registro para atualizar!")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE usuarios
                SET nome = ?, email = ?, telefone = ?
                WHERE id = ?
            """, (self.nome.get(), self.email.get(), self.telefone.get(), self.id.get()))
            self.conn.commit()
            
            self.limpar_campos()
            self.carregar_dados()
            messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar registro: {str(e)}")
    
    def deletar_registro(self):
        if not self.id.get():
            messagebox.showerror("Erro", "Por favor, selecione um registro para deletar!")
            return
        
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar este registro?"):
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id = ?", (self.id.get(),))
                self.conn.commit()
                
                self.limpar_campos()
                self.carregar_dados()
                messagebox.showinfo("Sucesso", "Registro deletado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar registro: {str(e)}")
    
    def carregar_dados(self):
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Carregar dados do banco
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        
        for row in rows:
            self.tree.insert("", "end", values=row)
    
    def selecionar_item(self, event):
        try:
            # Obter item selecionado
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item)['values']
            
            # Preencher campos
            self.id.set(values[0])
            self.nome.set(values[1])
            self.email.set(values[2])
            self.telefone.set(values[3])
        except IndexError:
            pass
    
    def limpar_campos(self):
        self.id.set('')
        self.nome.set('')
        self.email.set('')
        self.telefone.set('')

if __name__ == '__main__':
    root = tk.Tk()
    app = AplicacaoCRUD(root)
    root.mainloop()