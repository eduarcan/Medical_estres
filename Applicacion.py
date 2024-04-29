import tkinter as tk
from tkinter import messagebox
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import load_model
c=0
puntuacion_total=0
#Resp_preg=[5, 1, 5, 2, 2, 5, 3, 1, 1, 1, 1, 5, 1, 1, 5, 5, 5, 5, 1, 5, 1, 5, 1, 5, 1, 1, 5, 1, 2, 5]
Resp_preg=[]
class PreguntasApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Cuestionario")
        self.root.geometry("600x200")
        self.pregunta1()

    def pregunta1(self):
        global c
        c=c+1
        
        self.respuesta1 = tk.IntVar()
        
        pregunta_frame = tk.Frame(self.root, padx=10, pady=10)
        pregunta_frame.pack()

        if (c==1):
            t="Soy feliz: ¿Cómo calificarías esto?"
        elif (c==2):
            t="Estoy preocupado por una o más personas \na las que he ayudado o ayudo: \n¿Cómo calificarías esto?"
        elif (c==3):
            t="Estoy satisfecho de poder ayudar a la gente\n ¿Cómo calificarías esto?"
        elif (c==4):
            t="Me siento vinculado a otras personas, \n con ocasión de mi trabajo\n ¿Cómo calificarías esto?"
        elif (c==5):
            t="Me sobresaltan los sonidos inesperados. \n¿Cómo calificarías esto?"
        elif (c==6):
            t="Me siento fortalecido después de trabajar \n con las personas a las que he ayudado \n¿Cómo calificarías esto?"
        elif (c==7):
            t="Encuentro difícil separar mi vida personal \n de mi vida profesional. \n¿Cómo calificarías esto?"
        elif (c==8):
            t="Pierdo el sueño por las experiencias \n traumáticas de las personas a las que he ayudado. \n¿Cómo calificarías esto?"
        elif (c==9):
            t="Creo que he sido afectado negativamente \n por las experiencias traumáticas de aquellos a \n quienes he ayudado. \n¿Cómo calificarías esto?"
        elif (c==10):
            t="Me siento 'atrapado' por mi trabajo. \n¿Cómo calificarías esto?"
        elif (c==11):
            t="Debido a mi profesión tengo la sensación \n de estar al límite en varias cosas. \n¿Cómo calificarías esto?"
        elif (c==12):
            t="Me gusta trabajar ayudando a la gente. \n¿Cómo calificarías esto?"
        elif (c==13):
            t="Me siento deprimido como resultado de mi trabajo. \n¿Cómo calificarías esto?"
        elif (c==14):
            t="Me siento como si fuera yo el que experimenta \n el trauma de alguien al que he ayudado. \n¿Cómo calificarías esto?"
        elif (c==15):
            t="Tengo creencias (religiosas, espirituales u otras)\n que me apoyan en mi trabajo profesional. \n¿Cómo calificarías esto?"
        elif (c==16):
            t="Estoy satisfecho por cómo soy capaz de mantenerme \n al día en las técnicas y procedimientos \n de asistencia médica. \n¿Cómo calificarías esto?"
        elif (c==17):
            t="Soy la persona que siempre he querido ser. \n¿Cómo calificarías esto?"
        elif (c==18):
            t="Mi trabajo me hace sentirme satisfecho. \n¿Cómo calificarías esto?"
        elif (c==19):
            t="Por causa de mi trabajo me siento agotado. \n¿Cómo calificarías esto?"
        elif (c==20):
            t="Tengo pensamientos de satisfacción \n acerca de las personas a las que he \n ayudado y sobre cómo he podido ayudarles. \n¿Cómo calificarías esto?"
        elif (c==21):
            t="Me siento abrumado por la cantidad y tipo de trabajo que tengo que afrontar. \n¿Cómo calificarías esto?"
        elif (c==22):
            t="Creo que puedo hacer cambiar las cosas a través de mi trabajo. \n¿Cómo calificarías esto?"
        elif (c==23):
            t="Evito ciertas actividades o situaciones \n porque me recuerdan a las experiencias espantosas\n de la gente a la que he ayudado. \n¿Cómo calificarías esto?"
        elif (c==24):
            t="Planeo continuar con mi trabajo por muchos años. \n¿Cómo calificarías esto?"
        elif (c==25):
            t="Como resultado de mi trabajo profesional,\n tengo pensamientos molestos, repentinos, indeseados. \n¿Cómo calificarías esto?"
        elif (c==26):
            t="Me siento 'estancado' (sin saber qué hacer) \n por como funciona el sistema sanitario. \n¿Cómo calificarías esto?"
        elif (c==27):
            t="Considero que soy un buen profesional. \n¿Cómo calificarías esto?"
        elif (c==28):
            t="No puedo recordar determinados acontecimientos \n relacionados con víctimas muy traumáticas. \n¿Cómo calificarías esto?"
        elif (c==29):
            t="Soy una persona demasiado sensible. \n¿Cómo calificarías esto?"
        elif (c==30):
            t="Estoy feliz por haber elegido hacer este trabajo. \n¿Cómo calificarías esto?"
        else:
            self.mostrar_puntuacion()
        try:
            
            label_pregunta = tk.Label(pregunta_frame, text=t)
            label_pregunta.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

            for i in range(1, 6):
                tk.Radiobutton(pregunta_frame, text=str(i), variable=self.respuesta1, value=i).grid(row=1, column=i-1)
            
            siguiente_button = tk.Button(pregunta_frame, text="Siguiente", command=lambda: self.siguiente_pregunta(pregunta_frame))
            siguiente_button.grid(row=2, column=0, columnspan=5, pady=10)
        except:
            pass

    def siguiente_pregunta(self, pregunta_frame):
        global puntuacion_total
        global Resp_preg
        global c
        Resp_preg.append(self.respuesta1.get())
        
        puntuacion_total = self.respuesta1.get() + puntuacion_total
        pregunta_frame.destroy()  # Elimina la ventana de la pregunta 1
        #print (puntuacion_total)
        if (c<30):
            self.pregunta1()
        else:
            self.mostrar_puntuacion(pregunta_frame)

    def mostrar_puntuacion(self,pregunta_frame):
        global puntuacion_total
        global Resp_preg
        import tensorflow as tf
        from tensorflow.keras.models import load_model

        pregunta_frame.destroy()
        #pregunta_frame.geometry("800x200")
        pregunta_frame = tk.Frame(self.root, padx=10, pady=10)
        pregunta_frame.pack()
        
        
        model=load_model('red_Trauma_stres_CS_3.h5')
        model_sts=load_model('red_Trauma_stres_sts_1.h5')
        model_burnout=load_model('red_Trauma_stres_burnout.h5')
        
        dt=np.array(Resp_preg)
        dt = dt.reshape(1, -1)
        predictions_cs = model.predict(dt)
        predictions_sts = model_sts.predict(dt)
        predictions_burnout = model_burnout.predict(dt)
 

        if ((predictions_cs[0][0]>predictions_cs[0][1])):
            #print("CS bajo")
            Predic_CS = tk.Button(pregunta_frame, text="CS no presente",bg='green')         
            Predic_CS.grid(row=1, column=0, columnspan=5, pady=10)

        if ((predictions_cs[0][1]>predictions_cs[0][0])):
        #    print("CS medio")
            Predic_CS = tk.Button(pregunta_frame, text="CS presente",bg='red')         
            Predic_CS.grid(row=1, column=0, columnspan=5, pady=10)


        if (predictions_sts[0][0]>predictions_sts[0][1]):
            #print("No presencia de STS")
            Predic_sts = tk.Button(pregunta_frame, text="Sin STS",bg='green')         
            Predic_sts.grid(row=2, column=0, columnspan=5, pady=10)
        else:
            #print("Presencia de STS")
            Predic_sts = tk.Button(pregunta_frame, text="Con STS",bg='red')         
            Predic_sts.grid(row=2, column=0, columnspan=5, pady=10)

        if (predictions_burnout[0][0]>predictions_burnout[0][1]):
            #print("No presencia de burnout")
            Predic_burnout = tk.Button(pregunta_frame, text="Sin burnout",bg='green')         
            Predic_burnout.grid(row=3, column=0, columnspan=5, pady=10)
        else:
            Predic_burnout = tk.Button(pregunta_frame, text="con burnout",bg='red')         
            Predic_burnout.grid(row=3, column=0, columnspan=5, pady=10)
            #print("Presencia de burnout")

        #Salir = tk.Button(pregunta_frame, text="Salir",command=lambda: self.salir(pregunta_frame))         
        #Salir.grid(row=4, column=1, columnspan=5, pady=10)

        Reiniciar = tk.Button(pregunta_frame, text="Reiniciar",command=lambda: self.reiniciar(pregunta_frame))         
        Reiniciar.grid(row=4, column=1, columnspan=5, pady=10)
        print (Resp_preg)

#    def salir(self,pregunta_frame):
 #       pregunta_frame.destroy()
        #exit()
    def reiniciar(self,pregunta_frame):
        global c
        c=0
        Resp_preg=[]
        pregunta_frame.destroy()
        self.pregunta1()
       
        

if __name__ == "__main__":
    root = tk.Tk()
    app = PreguntasApp(root)
    root.mainloop()
