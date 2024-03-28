import customtkinter

############################# Estabeleci variáveis para os números
# Keys Numbers                Acredito ter um método mais eficiente.
#############################
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9
n0 = 0
############################# A mesma coisa para as telas da calculadora
# Screen Variables            Funcionam como duas telas de cálculo e uma  
############################# de resultado.  
screen_main = []
screen_second = []
sm_str = ''
ss_str = ''
float_key = '.'
operation = []
calc = operation

############################# Variáveis da tela de total que serão 
# Total Screen Variables      alteradas em função posterior.  
#############################
final_screen = ''
v_total = ''

############################# Configuração da tela principal pelo
# Main Window                 customtkinter  
#############################
theme = ''
app = customtkinter.CTk()
app.geometry("260x400")
app.title("Calculadora")
app.resizable(width=False, height=False)
customtkinter.set_appearance_mode('light')
darktheme = []
theme = ''

############################# Fundo da aplicação, há com toda certeza uma 
# Background                  maneira simplificada de chegar ao mesmo resultado!
############################# Mas para minha leitura ficou mais objetivo dessa forma.
bg1 = customtkinter.CTkLabel(app, text='', fg_color=('#ffffff','#110f0f'), width=1000, height=1000)
bg1.place(relx=0, rely=0)
bg = customtkinter.CTkLabel(app, text='', fg_color=('#bcbcbc','#262c30'), width=1000, height=1000)
bg.place(relx=0, rely=0.4)


############################# Defini todas as funções dos botões abaixo, li alguns
# Buttons Functions           materiais que utilizaram lambda. Porém no momento
############################# ainda não possuo conhecimento para aplicar desta maneira
def press_0():
    screen_second.append(+0)
    if calc == ['+']:
        screen_second.append(+0)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+0)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+0)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+0)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+0)
        screen_label.configure(text=screen_main)

def press_1():
    if calc == ['+']:
        screen_second.append(+1)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+1)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+1)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+1)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+1)
        screen_label.configure(text=screen_main)


def press_2():
    if calc == ['+']:
        screen_second.append(+2)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+2)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+2)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+2)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+2)
        screen_label.configure(text=screen_main)


def press_3():
    if calc == ['+']:
        screen_second.append(+3)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+3)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+3)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+3)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+3)
        screen_label.configure(text=screen_main)


def press_4():
    if calc == ['+']:
        screen_second.append(+4)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+4)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+4)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+4)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+4)
        screen_label.configure(text=screen_main)


def press_5():
    if calc == ['+']:
        screen_second.append(+5)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+5)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+5)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+5)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+5)
        screen_label.configure(text=screen_main)


def press_6():
    if calc == ['+']:
        screen_second.append(+6)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+6)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+6)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+6)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+6)
        screen_label.configure(text=screen_main)

def press_7():
    if calc == ['+']:
        screen_second.append(+7)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+7)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+7)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+7)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+7)
        screen_label.configure(text=screen_main)


def press_8():
    if calc == ['+']:
        screen_second.append(+8)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+8)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+8)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+8)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+8)
        screen_label.configure(text=screen_main)


def press_9():
    if calc == ['+']:
        screen_second.append(+9)
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append(+9)
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append(+9)
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append(+9)
        screen_label.configure(text=screen_second)
    else:
        screen_main.append(+9)
        screen_label.configure(text=screen_main)


def clear_all():
    operation.clear()
    screen_main.clear()
    screen_second.clear()
    screen_label.configure(text='0')
    

def somar():
    operation.clear()
    operation.append('+')
    calc = '+'
    screen_label.configure(text=screen_second)



def sub():
    operation.clear()
    operation.append('-')
    calc = '-'
    screen_label.configure(text=screen_second)



def mult():
    operation.clear()
    operation.append('*')
    calc = '*'
    screen_label.configure(text=screen_second)



def dividir():
    operation.clear()
    operation.append('/')
    calc = '/'
    screen_label.configure(text=screen_second)


        
def float_num():
    if calc == ['+']:
        screen_second.append('.')
        screen_label.configure(text=screen_second)
    elif calc == ['-']:
        screen_second.append('.')
        screen_label.configure(text=screen_second)
    elif calc == ['*']:
        screen_second.append('.')
        screen_label.configure(text=screen_second)
    elif calc == ['/']:
        screen_second.append('.')
        screen_label.configure(text=screen_second)
    else:
        screen_main.append('.')
        screen_label.configure(text=screen_main)


def total():                                # Uma menção especial a esta parte do código
                                            # Toda a parte lógica para o resultado final e funcionamento                  
    sm_str = str(screen_main)               # Acontece aqui seguindo o seguinte roteiro:                     
    sm_str = sm_str.strip('[]')             
    sm_str = sm_str.replace(',','')         # Os número estão em uma lista -> Convertida em String ->
    sm_str = sm_str.replace(' ','')         # São retirados da string: colchetes, vírgulas e aspas simples ->
    sm_str = sm_str.replace("'",'')         # Utilizando If ele irá verificar a presença do ponto flutuante ou não ->
    if float_key not in sm_str:              # Após isso o resultado é exibido como float ou int.
        sm_float = int(sm_str)
    else:
        sm_float = float(sm_str)    


    ss_str = str(screen_second)
    ss_str = ss_str.strip('[]')
    ss_str = ss_str.replace(',','')
    ss_str = ss_str.replace(' ','')
    ss_str = ss_str.replace("'",'')
    if float_key not in ss_str:
        ss_float = int(ss_str)
    else:
        ss_float = float(ss_str)


    if calc == ['+']:
        v_total = sm_float + ss_float
        screen_label.configure(text=v_total)
    elif calc == ['-']:
        v_total = sm_float - ss_float
        screen_label.configure(text=v_total)
    elif calc == ['*']:
        v_total = sm_float * ss_float
        screen_label.configure(text=v_total)
    elif calc == ['/']:
        v_total = sm_float / ss_float
        screen_label.configure(text=v_total)

    operation.clear()                       # Assumi que seria mais simples após o resultado ser exibido
    screen_main.clear()                     # que a calculadora fosse limpa para um input de novos calculos.
    screen_second.clear()


############################# Funções para alterar o tema.  
# Theme Keys                 A lógica funciona checkando se o número é impa ou par.
############################# Caso "par" o tema é definido como claro e o contrário para escuro.
def theme_mode():
    darktheme.append(1)
    theme = str(darktheme)
    theme = theme.strip('[]')
    theme = theme.replace(',','')
    theme = theme.replace(' ','')
    theme = theme.replace("'",'')
    theme = len(theme)
    if theme % 2 == 0:
        customtkinter.set_appearance_mode('light')
        theme_button.configure(text='Dark Mode')
    else:
        customtkinter.set_appearance_mode('dark')
        theme_button.configure(text='Light Mode')


############################# Todos os botões numéricos utilizados no projeto  
# Button Keys                 
############################# 
b0 = customtkinter.CTkButton(app, text="0", command=press_0, width=106, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))

b0.place(relx=0.05, rely=0.86)

b1 = customtkinter.CTkButton(app, text="1", command=press_1, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))

b1.place(relx=0.05, rely=0.74)

b2 = customtkinter.CTkButton(app, text="2", command=press_2, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b2.place(relx=0.29, rely=0.74)

b3 = customtkinter.CTkButton(app, text="3", command=press_3, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b3.place(relx=0.52, rely=0.74)

b4 = customtkinter.CTkButton(app, text="4", command=press_4, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b4.place(relx=0.05, rely=0.62)

b5 = customtkinter.CTkButton(app, text="5", command=press_5, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b5.place(relx=0.29, rely=0.62)

b6 = customtkinter.CTkButton(app, text="6", command=press_6, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b6.place(relx=0.52, rely=0.62)

b7 = customtkinter.CTkButton(app, text="7", command=press_7, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b7.place(relx=0.05, rely=0.50)

b8 = customtkinter.CTkButton(app, text="8", command=press_8, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b8.place(relx=0.29, rely=0.50)

b9 = customtkinter.CTkButton(app, text="9", command=press_9, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                             bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color=('#110d0d','#ffffff'))
b9.place(relx=0.52, rely=0.50)

############################# Estou estudando a implementação de novas operações
# Operations Buttons          Ex: Números negativos, porcentagem, potência e afins...
#############################

sum_button = customtkinter.CTkButton(app, text="+", command=somar, width=50, height=35, fg_color=('#ffffff','#110d0d'),
                                     bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 20), text_color='#e65338')
sum_button.place(relx=0.75, rely=0.42)

sub_button = customtkinter.CTkButton(app, text="-", command=sub, width=50, height=35, fg_color=('#ffffff','#110d0d'),
                                     bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 20), text_color='#e65338')
sub_button.place(relx=0.75, rely=0.52)

mult_button = customtkinter.CTkButton(app, text="x", command=mult, width=50, height=35, fg_color=('#ffffff','#110d0d'),
                                      bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 20), text_color='#e65338')
mult_button.place(relx=0.75, rely=0.62)

div_button = customtkinter.CTkButton(app, text="÷", command=dividir, width=50, height=35, fg_color=('#ffffff','#110d0d'),
                                     bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 20), text_color='#e65338')
div_button.place(relx=0.75, rely=0.72)


#############################
# System Buttons
#############################
clear_button = customtkinter.CTkButton(app, text="C", command=clear_all, width=50, height=18, fg_color=('#ffffff','#110d0d'),
                                       bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 16), text_color='#28935C')
clear_button.place(relx=0.05, rely=0.42)

theme_button = customtkinter.CTkButton(app, text="Dark Mode", command=theme_mode, width=113, height=18, fg_color=('#110d0d','#ffffff'),
                                       bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 15), text_color=('#f1c232','#110d0d'))
theme_button.place(relx=0.29, rely=0.42)

float_button = customtkinter.CTkButton(app, text=",", command=float_num, width=50, height=40, fg_color=('#ffffff','#110d0d'),
                                       bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 25), text_color='#f1c232')
float_button.place(relx=0.52, rely=0.86)

total_button = customtkinter.CTkButton(app, text="=", command=total, width=50, height=55, fg_color=('#ffffff','#110d0d'),
                                       bg_color=('#bcbcbc','#262c30'),font=('Doradani Bold', 20), text_color='#e65338')
total_button.place(relx=0.75, rely=0.83)

screen_label = customtkinter.CTkLabel(app, text='0', fg_color=('#ffffff','#110f0f'), width=300, height=100, anchor='center',
                                      font=('Doradani Bold', 30), text_color=('#110f0f','#ffffff'))

screen_label.place(relx=0.13, rely=0.1)
app.mainloop()