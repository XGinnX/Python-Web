# Titulo: ChatZap
# 1. Botão de Iniciar
    # 1.1 Abre Pop Up/ Modal ao clicar no botão
        # 1.1.1 Modal deve possuir
         # Titulo: Bem vindo ao ChatZap
         # campo: Escreva seu nome no chatZap
         # botão: Entre no chat
# 2. Chat
 #2.1. Espaço CHat de mensagens
 #2.2. A Baixo do espaço de chat deve possuir:
       # Campo Digite a sua mensagem
       # botão de enviar
       
# Passo a passo para utilizar o FLET
       
import flet as ft # 1. Importar

def main (pagina): # 2. criar função principal
    texto = ft.Text("ChatZap")
    
    chat = ft.Column()
    
    def enviar_mensagem(evento):
        texto_mensagem = ft.Text(campo_mensagem.value)
        chat.controls.append(texto_mensagem)
        print("mensagem Enviada")
        campo_mensagem.value = ""
        pagina.update()
           
    campo_mensagem = ft.TextField(label="Digite a sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem,botao_enviar])
    
    def entrar_no_chat(evento):
         print("Entrar no chat")
         popup.open=False
         pagina.remove(texto)
         pagina.remove(botao_iniciar)
         pagina.add(chat)
         texto_entrada = ft.Text(f"{nome_usuario.value} entrou no chat")
         chat.controls.append(texto_entrada)
         pagina.add(linha_enviar)
         pagina.update()
    
    titulo_popup = ft.Text("Bem vindo ao ChatZap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)
    
    popup = ft.AlertDialog(
       open=False,
       modal=True,
       title=titulo_popup,
       content=nome_usuario,
       actions=[botao_entrar]
    )
    
    def abrir_popup(evento):
     print("Abrir o chat")
     pagina.dialog = popup
     popup.open = True
     pagina.update()
     
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)    
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main) # criar o app chamando a função principal