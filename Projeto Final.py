from tkinter import *
import customtkinter
import qrcode
from hashlib import md5
import json

banco_dados = {}
banco_email = {}


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
tela_cadastro = customtkinter.CTk()
tela_cadastro.geometry("855x600")
tela_cadastro.title("Cadastro")

largura_tela = tela_cadastro.winfo_screenwidth()
altura_tela = tela_cadastro.winfo_screenheight()

pos_x = (largura_tela - 855) // 2
pos_y = (altura_tela - 600) // 2


tela_cadastro.tk.call('wm', 'geometry', tela_cadastro, f"855x600+{pos_x}+{pos_y}")


texto_tela1 = customtkinter.CTkLabel(tela_cadastro, text = "Olá, visualize os lugares ofertados e quando estiver preparado execute seu cadastro!")
texto_tela1.pack(padx = 10, pady = 10)


imagem_poltrona = PhotoImage(file="PYTHON\Projeto 2\PoltronaCinemaP.png")
png_poltrona = Label(image=imagem_poltrona)
png_poltrona.pack(padx=10, pady=10)


def clique_cadastro():
    
    tela_dados = customtkinter.CTkToplevel()
    tela_dados.attributes('-topmost', True)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    tela_dados.geometry("855x600")
    tela_dados.title("Dados_user")

    largura_tela = tela_dados.winfo_screenwidth()
    altura_tela = tela_dados.winfo_screenheight()

    pos_x = (largura_tela - 855) // 2
    pos_y = (altura_tela - 600) // 2


    tela_dados.tk.call('wm', 'geometry', tela_dados, f"855x600+{pos_x}+{pos_y}")

    texto_preencher_dados = customtkinter.CTkLabel(tela_dados, text = "Vamos preencher seus dados:")
    texto_preencher_dados.pack(padx = 10, pady = 10)
    
    selecao_poltrona = customtkinter.CTkEntry(tela_dados, placeholder_text= "lugar escolhido")
    selecao_poltrona.pack(padx = 10, pady = 10)

    cpf_user = customtkinter.CTkEntry(tela_dados, placeholder_text= "CPF")
    cpf_user.pack(padx = 10, pady = 10)
    
    email_user = customtkinter.CTkEntry(tela_dados, placeholder_text= "Seu melhor E-mail")
    email_user.pack(padx = 10, pady = 10)


    def salvar_dados():
        
        criptografia = cpf_user.get().encode("utf8")
        
        hash_criptografia = md5(criptografia).hexdigest()
        
        imagem = qrcode.make(hash_criptografia)

        imagem.save(f"QR_code{selecao_poltrona.get()}.png")

        banco_dados[selecao_poltrona.get()] = hash_criptografia

        banco_email[selecao_poltrona.get()] = email_user.get()

    def sair_tela_dados():
        tela_dados.destroy()


    salvar_dados_botao_cadastro = customtkinter.CTkButton(tela_dados, text = "Salvar informações", command = salvar_dados)
    salvar_dados_botao_cadastro.pack(padx = 10, pady = 10)

    botao_voltar_inicio = customtkinter.CTkButton(tela_dados, text = "Voltar", command = sair_tela_dados)
    botao_voltar_inicio.pack(padx = 10, pady = 10)


cadastro_botao = customtkinter.CTkButton(tela_cadastro, text = "Cadastro", command = clique_cadastro)
cadastro_botao.pack(padx = 10, pady = 10)


def clique_abir_opcoes():
    tela_opcoes_admin = customtkinter.CTkToplevel()
    tela_opcoes_admin.attributes('-topmost', True)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    tela_opcoes_admin.geometry("855x600")
    tela_opcoes_admin.title("Dados_user")

    largura_tela = tela_opcoes_admin.winfo_screenwidth()
    altura_tela = tela_opcoes_admin.winfo_screenheight()

    pos_x = (largura_tela - 855) // 2
    pos_y = (altura_tela - 600) // 2


    tela_opcoes_admin.tk.call('wm', 'geometry', tela_opcoes_admin, f"855x600+{pos_x}+{pos_y}")

    def consultar_BD():
        tela_consulta = customtkinter.CTkToplevel()
        tela_consulta.title("Banco de dados")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        tela_consulta.geometry("855x600")

        largura_tela = tela_consulta.winfo_screenwidth()
        altura_tela = tela_consulta.winfo_screenheight()

        pos_x = (largura_tela - 855) // 2
        pos_y = (altura_tela - 600) // 2


        tela_consulta.tk.call('wm', 'geometry', tela_consulta, f"855x600+{pos_x}+{pos_y}")
        
        texto_tela_consulta = customtkinter.CTkLabel(tela_consulta, text = "Aqui está o bando de dados: ")
        texto_tela_consulta.pack(padx = 10, pady = 10)
        
        texto_banco_dados = customtkinter.CTkLabel(tela_consulta, text = len(banco_dados))
        texto_banco_dados.pack(padx = 10, pady = 10)
        

        if botao_consultBD:
            tela_opcoes_admin.destroy()

        def sair_tela_consulta():
            tela_consulta.destroy() 

        def copy_cpf_dic():
            code_cpf_json = json.dumps(banco_dados)
            with open("dicCPF.json", "w") as json_file:
                json_file.write(code_cpf_json)
            print(banco_dados)

        def copy_email_dic():
            print(banco_email)


        copiar_botao_cpf = customtkinter.CTkButton(tela_consulta, text = "copy banco de dados CPF", command = copy_cpf_dic) 
        copiar_botao_cpf.pack(padx = 10, pady = 10)

        copiar_botao_email = customtkinter.CTkButton(tela_consulta, text = "copy banco de dados E-mail", command = copy_email_dic)
        copiar_botao_email.pack(padx = 10, pady = 10)

        sair_cadastro_botao = customtkinter.CTkButton(tela_consulta, text = "Voltar", command = sair_tela_consulta)
        sair_cadastro_botao.pack(padx = 10, pady = 10)



    def limpar_BD():
        banco_dados.clear()
        banco_email.clear()

        if limpar_BD:
            tela_opcoes_admin.destroy()
    
    
    def voltar_tela_poltrona():
        tela_opcoes_admin.destroy()
    

    def tela_excluir_poltrona():
        tela_excluir_poltrona = customtkinter.CTkToplevel()
        tela_excluir_poltrona.attributes('-topmost', True)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        tela_excluir_poltrona.geometry("855x600")
        tela_excluir_poltrona.title("Dados_user")

        largura_tela = tela_excluir_poltrona.winfo_screenwidth()
        altura_tela = tela_excluir_poltrona.winfo_screenheight()

        pos_x = (largura_tela - 855) // 2
        pos_y = (altura_tela - 600) // 2


        tela_excluir_poltrona.tk.call('wm', 'geometry', tela_excluir_poltrona, f"855x600+{pos_x}+{pos_y}")


        if tela_excluir_poltrona:
            tela_opcoes_admin.destroy()


        def sair_exclusão():
            tela_excluir_poltrona.destroy()

        texto_excluir = customtkinter.CTkLabel(tela_excluir_poltrona, text = "Para excluir um cadastro preencha os dados: ")
        texto_excluir.pack(padx = 10, pady = 10)
        
        poltrona_excluir = customtkinter.CTkEntry(tela_excluir_poltrona, placeholder_text= "Digite o número ")
        poltrona_excluir.pack(padx = 10, pady = 10)
        
        
        cpf_excluir = customtkinter.CTkEntry(tela_excluir_poltrona, placeholder_text= "Digite o CPF")
        cpf_excluir.pack(padx = 10, pady = 10)
        
        
        def excluir_cadastro():
            
            del banco_dados[poltrona_excluir.get()]
            del banco_email[poltrona_excluir.get()]
        

        botao_excluir = customtkinter.CTkButton(tela_excluir_poltrona, text = "Excluir", command = excluir_cadastro) 
        botao_excluir.pack(padx = 10, pady = 10)
        
        
        botao_voltar_excluir = customtkinter.CTkButton(tela_excluir_poltrona, text = "Voltar", command = sair_exclusão)
        botao_voltar_excluir.pack(padx = 10, pady = 10)

        
        
    botao_consultBD = customtkinter.CTkButton(tela_opcoes_admin, text = "Visualizar a quantidade de cadastros", command = consultar_BD)
    botao_consultBD.pack(padx = 10, pady = 10)

    botao_limparBD = customtkinter.CTkButton(tela_opcoes_admin, text = "Limpar banco de dados", command = limpar_BD)
    botao_limparBD.pack(padx = 10, pady = 10)

    botao_abrir_tela_excluir = customtkinter.CTkButton(tela_opcoes_admin, text = "Excluir cadastro", command = tela_excluir_poltrona)
    botao_abrir_tela_excluir.pack(padx = 10, pady = 10)

    botao_voltar_inicio = customtkinter.CTkButton(tela_opcoes_admin, text = "Voltar", command = voltar_tela_poltrona)
    botao_voltar_inicio.pack(padx = 10, pady = 10)


opcoes_admin_botao = customtkinter.CTkButton(tela_cadastro, text = "Opções", command = clique_abir_opcoes)
opcoes_admin_botao.pack(padx = 10, pady = 10)


def fechar_app():
    quit()

botao_fechar_app = customtkinter.CTkButton(tela_cadastro, text = "Sair", command = fechar_app)
botao_fechar_app.pack(padx = 10, pady = 10)


tela_cadastro.mainloop()