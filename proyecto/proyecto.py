import pygame, random, os
#nivel 5
def vamosBorrar():
  if os.name == "posix":
     os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
     os.system ("cls")
def nivel5():
    file = 'musicafondo.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    print("Pregunta n°5 y final")
    print("Selecciona la letra de la respuesta a la siguiente pregunta")
    print("¿El contacto a tus mascotas puede propagar la enfermedad?")
    print("a. No")
    print("b. Sí")
    print()
    Respuesta5=input("Seleccione la letra que corresponde a la respuesta correcta ")
    print()
    if Respuesta5!="b":
        print("Mal, respuesta incorrecta, tu bola será más pequeña, presiona enter para continuar")
        input("preiona enter para continuar")
        radiopildora=10
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora2.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()
    elif Respuesta5=="b":
        print("Es correcto!, tus animales por medio de sus patas pueden contener el virus, tu bola ahora será más grande")
        input("presiona enter para continuar")
        radiopildora=35
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora3.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()

    vamosBorrar()

    life=3

    posicionbolax=400-radiopildora
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
        
    Negro = (0,0,0)
    Blanco = (255,255,255)

  
    class virus1(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus1.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus2(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus2.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus3(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus3.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus4(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus4.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus5(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus5.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()
                              

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()


    for i in range(5):
        x=1
        
        while x<800:
            if i==0:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==1:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==2:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==3:
                bloque=virus4()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            elif i==4:
                bloque=virus5()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5


        posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)


    fluid=True
    fondo = pygame.image.load("Fondo.png").convert()

    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-75
        rect2=rect+75
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False

            if i.type==pygame.MOUSEBUTTONDOWN:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
                
        ventana.blit(fondo,[0,0])
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax==radiopildora:
            velocidadx*= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay==radiopildora:
            velocidady*= -1
        
        todosObjetos.draw(ventana)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
            
         
        if punto3.colliderect(medic)or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1

        if life==0 or len(virusLista)==0:
            fluid=False                

        pygame.display.flip()
    print("game over")
    pygame.quit()

#nivel 2
def nivel2():
    life=3
    print("Pregunta n°2")
    print("Selecciona la letra de la respuesta a la siguiente pregunta")
    print("¿Cuáles son los síntomas más comunes a la hora de enfermarse con coronavirus?")
    print("a. Diarrea y dolor de cabeza")
    print("b. Dolor de garganta y conjuntivitis")
    print("c. Erupciones, pérdida del apetito y del olfato")
    print("d. Fiebre, tos seca y cansancio")
    print()
    Respuesta2=input("Selecciona la letra que corresponde a la respuesta correcta: ")
    print()
    if Respuesta2!="d":
        print("Mal, respuesta incorrecta, tu bola será más pequeña, presiona enter para seguir")
        input()
        radiopildora=10
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora2.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()
    elif Respuesta2=="d":
        radiopildora=20
        print("Es correcto!, tienes una vida extra")
        print("Presiona enter para continuar")
        input()
        life+=1
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()
    vamosBorrar()
        
    posicionbolax=400-radiopildora
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
        
    Negro = (0,0,0)
    Blanco = (255,255,255)
    
    mediclado=75
    class medic(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("medic.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect = self.image.get_rect()

    class virus1(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus1.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus2(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus2.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus3(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus3.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus4(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus4.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus5(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus5.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(6):
        x=1
        if i==0:
            while x<800:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31
        elif i==1:
            x=61.5
            while x<737:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==2:
            x=123
            while x<676:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==3:
            x=184
            while x<614:
                bloque=virus4()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==4:
            x=246
            while x<553:
                bloque=virus5()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31

        elif i==5:
            x=307.5
            while x<492:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

            posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-mediclado
        rect2=rect+mediclado
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
        
        ventana.blit(fondo,[0,0])
                
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax<=radiopildora:
            velocidadx *= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay<=radiopildora:
            velocidady *= -1
        
        todosObjetos.draw(ventana)
        punto1=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay-radiopildora),0)
        punto2=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay-radiopildora),0)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1
        if life==0 or len(virusLista)==0:
            fluid=False        

        pygame.display.flip()

    pygame.quit()
#nivel 4
def nivel4():
    print("Pregunta n°4")
    print("Selecciona la letra de la respuesta a la siguiente pregunta")
    print("¿Qué debo hacer si me enfermo de covid-19?")
    print("a. Quedarme en mi hogar")
    print("b. Ir directamente al hospital")
    print("c. Seguir saliendo a las calles")
    print()
    Respuesta4=input("Seleccione la letra que corresponde a la respuesta correcta ")
    print()
    
    if Respuesta4!="a":
        print("Mal, respuesta incorrecta, si te enfermas de coronavirus, lo mejor es quedarte en tu casa ya que así no enfermarás a más personas que las que ya has infectado, tu barra sera mas pequeña, presiona enter para continuar")
        input()
        mediclado=50
        class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic2.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()
    elif Respuesta4=="a":
        print("Es correcto!, aunque suene macabro, si te quedas en tu hogar no enfermas más personas que las que conviven contigo, suponiendo que estas ya están enfermas por tu culpa, tu barra sera mas grande")
        print("Presiona enter para continuar")
        input()
        mediclado=100
        class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic3.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()

    vamosBorrar()
    
    posicionbolax=380
    posicionbolay=400

    life=3

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
    
    Negro = (0,0,0)
    Blanco = (255,255,255)

    class virus(pygame.sprite.Sprite):
            def __init__(selfi):
                super().__init__()
                selfi.image = pygame.image.load("virus2.png").convert()
                selfi.image.set_colorkey(Blanco)
                selfi.rect=selfi.image.get_rect()
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    x=170
    while x<600:        
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31
    for i in range(2):
        x=110
        while x<614:
                
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        posicionvirus1y+=31
        
    for i in range(2):
        x=110
        while x<233:
            
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        for i in range(2):
            x=355
            while x<410:
                bloque=virus()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

        for i in range(2):
            x=540
            while x<602:
            
                bloque=virus()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
    
        posicionvirus1y+=31

    for i in range(2):
        x=110
        while x<614:
                
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        posicionvirus1y+=31

    x=171
    while x<550:
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31

    x=232
    while x<500:
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

    posicionvirus1y+=31

    for i in range(2):
        x=232
        while x<290:            
            bloque=virus()
            bloque.rect.x = x
            bloque.rect.y = posicionvirus1y
            virusLista.add(bloque)
            todosObjetos.add(bloque)
            x+=61.5

        for i in range(4):
            x=355
            while x<410:                    
                bloque=virus()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5

        for i in range(4):
            x=478
            while x<535:            
                bloque=virus()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
    
        posicionvirus1y+=31

    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
            rectangulox=pygame.mouse.get_pos()   
            rect=rectangulox[0]
            rect1=rect-mediclado
            rect2=rect+mediclado

            for i in pygame.event.get(): 
                    if i.type==pygame.QUIT:
                            fluid=False
                            
                    if i.type==pygame.MOUSEBUTTONDOWN:
                        velocidadx=random.choice((-1,1))
                        velocidady=random.choice((-1,1))
                        musicafondo = 'musicafondo.mp3'
                        pygame.init()
                        pygame.mixer.init()
                        pygame.mixer.music.load(musicafondo)
                        pygame.mixer.music.play(-1)
                    
            ventana.blit(fondo,[0,0])
                
            if rect1>=0 and rect2<=800:
                    medic.rect.x=rect1

            medic.rect.y=500
            medicina.rect.x=posicionbolax-20
            medicina.rect.y=posicionbolay-20
            posicionbolax+=velocidadx
            posicionbolay+=velocidady
            if posicionbolax==800:
                    velocidadx*= -1
            elif posicionbolax==10:
                    velocidadx*= -1

            if posicionbolay==600:
                    posicionbolay = 300
                    life-=1
            elif posicionbolay==10:
                    velocidady*= -1

            todosObjetos.draw(ventana)
                
            punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-20,posicionbolay+20),0)
            punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+20,posicionbolay+20),0)
            if punto3.colliderect(medic) or punto4.colliderect(medic):
                    velocidady*= -1

            if pygame.sprite.spritecollide(medicina, virusLista , True):
                    velocidady*= -1

            if life==0 or len(virusLista)==0:
                    fluid=False

            pygame.display.flip()

    pygame.quit()
#nivel 3
def nivel3():
    print("Pregunta n°3")
    print("Selecciona la letra de la respuesta a la siguiente pregunta")
    print("¿Cuál es la forma más eficiente para protegerse del coronavirus?")
    print("a. Lavándose las manos")
    print("b. Lavándose los zapatos")
    print("c. Lavándose la cara")
    print("d. Lavándose el cuerpo entero")
    print()
    Respuesta3=input("Seleccione la letra que corresponde a la respuesta correcta ")
    print()
    if Respuesta3!="a":
        radiopildora=10
        print("Mal, respuesta incorrecta, tu bola será más pequeña, presiona enter para continuar")
        input()
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora2.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()

    elif Respuesta3=="a":
        radiopildora=35
        print("Es correcto!, tu bola ahora será más grande")
        print("Presiona enter para continuar")
        input()
        class medicina(pygame.sprite.Sprite):        
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("pildora3.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect=self.image.get_rect()

    vamosBorrar()
    
    posicionbolax=400-radiopildora
    posicionbolay=400

    life=3
    posicionvirus1y=1
    velocidadx=0
    velocidady=0
    
    Negro = (0,0,0)
    Blanco = (255,255,255)
    
    class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()

    class virus1(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus1.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus2(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus3.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus3(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus4.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class virus4(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus5.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)

    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(7):
        if i==0 or i==6:
            x=1
            while x<800:
                bloque=virus4()
                bloque.rect.x=x
                bloque.rect.y=posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            posicionvirus1y+=31
        elif i==3:
            x=1
            while x<800:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==308.5:
                    x+=123
                else:
                    x+=61.5
            posicionvirus1y+=31
        elif i==2 or i==4:
            x=1
            while x<800:
                bloque=virus2()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==247:
                    x+=246
                else:
                    x+=61.5
            posicionvirus1y+=31
        elif i==1 or i==5:
            x=1
            while x<800:
                bloque=virus3()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                if x==185.5:
                    x+=369
                else:
                    x+=61.5
            posicionvirus1y+=31
    
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo=pygame.image.load("Fondo.png").convert()
    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-75
        rect2=rect+75
    
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                musicafondo = 'musicafondo.mp3'
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(musicafondo)
                pygame.mixer.music.play(-1)
            
        ventana.blit(fondo,[0,0])
        
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500    
        medicina.rect.x=posicionbolax-radiopildora
        medicina.rect.y=posicionbolay-radiopildora
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==800-radiopildora:
            velocidadx*= -1
        elif posicionbolax==radiopildora:
            velocidadx*= -1
        
        if posicionbolay==600-radiopildora:
            posicionbolay = 300
            life-=1
        elif posicionbolay==radiopildora:
            velocidady*= -1
        
        todosObjetos.draw(ventana)
        punto1=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay-radiopildora),0)
        punto2=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay-radiopildora),0)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-radiopildora,posicionbolay+radiopildora),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+radiopildora,posicionbolay+radiopildora),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1

        if life==0 or len(virusLista)==0:
            fluid=False
        pygame.display.flip()

    pygame.quit()
#nivel 1
def nivel1():
    musicafondo = 'musicafondo.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(musicafondo)
    pygame.mixer.music.play(-1)
    print("Pregunta n°1")
    print("vamos a empezar con una pregunta")
    print("Selecciona la letra de la respuesta a la siguiente pregunta")
    print("¿Cuándo surgió el brote por coronavirus por primera vez en Wuhan?")
    print("a. En octubre de 2019")
    print("b. En noviembre de 2019")
    print("c. En diciembre de 2019")
    print("d. En enero de 2020")
    print()
    Respuesta1=input("Seleccione la letra que corresponde a la respuesta correcta ")
    print()
    if Respuesta1!="c":
        print("Mal, respuesta incorrecta, tu bola será pequeña, presiona enter para continuar")
        input()
        mediclado=50
        class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic2.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()
    elif Respuesta1=="c":
        print("Es correcto!, tu bola tendra el tamaño normal")
        print("Presiona enter para continuar")
        input()
        mediclado=75
        class medic(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("medic.png").convert()
                self.image.set_colorkey(Blanco)
                self.rect = self.image.get_rect()

    vamosBorrar()

    life=3
    posicionbolax=380
    posicionbolay=400

    posicionvirus1y=1
    velocidadx=0
    velocidady=0
        
    Negro = (0,0,0)
    Blanco = (255,255,255)

    class virus1(pygame.sprite.Sprite):
        def __init__(selfi):
            super().__init__()
            selfi.image = pygame.image.load("virus1.png").convert()
            selfi.image.set_colorkey(Blanco)
            selfi.rect=selfi.image.get_rect()
    class medicina(pygame.sprite.Sprite):        
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("pildora.png").convert()
            self.image.set_colorkey(Blanco)
            self.rect=self.image.get_rect()

    ventana = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Covid-Breaker")
    logo=pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    virusLista= pygame.sprite.Group()
    todosObjetos= pygame.sprite.Group()

    for i in range(10):
        x=1
        if i==0:
            x+=123
            while x<800:
                if x<245:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                elif 491>x>245:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=246
                elif 614>x>491:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=200
            posicionvirus1y+=31
        elif i==1:
            x+=61.5
            while x<800:
                if x<305:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                elif 428>x>305:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=123
                elif 735>x>428:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=500
            posicionvirus1y+=31
        elif i==2 or i==3:
            while x<800:
                bloque=virus1()
                bloque.rect.x = x
                bloque.rect.y = posicionvirus1y
                virusLista.add(bloque)
                todosObjetos.add(bloque)
                x+=61.5
            posicionvirus1y+=31
        elif i==4:
            x+=61.5
            while x<800:
                if x<735:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=200
            posicionvirus1y+=31
        elif i==5:
            x+=123
            while x<800:
                if x<674:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=200
            posicionvirus1y+=31
        elif i==6:
            x+=184.5
            while x<800:
                if x<610:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=300
            posicionvirus1y+=31
        elif i==7:
            x+=246
            while x<800:
                if x<520:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=500
            posicionvirus1y+=31
        elif i==8:
            x+=307.5
            while x<800:
                if x<450:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=700
            posicionvirus1y+=31
        elif i==9:
            x+=369
            while x<800:
                if x<400:
                    bloque=virus1()
                    bloque.rect.x = x
                    bloque.rect.y = posicionvirus1y
                    virusLista.add(bloque)
                    todosObjetos.add(bloque)
                    x+=61.5
                else:
                    x+=800
            posicionvirus1y+=31
    medicina= medicina()
    todosObjetos.add(medicina)
    medic=medic()
    todosObjetos.add(medic)

    fluid=True
    fondo = pygame.image.load("Fondo.png").convert()
    while fluid:
        rectangulox=pygame.mouse.get_pos()   
        rect=rectangulox[0]
        rect1=rect-mediclado
        rect2=rect+mediclado
        
        for i in pygame.event.get(): 
            if i.type==pygame.QUIT:
                fluid=False
            if i.type==pygame.MOUSEBUTTONDOWN:
                velocidadx=random.choice((-1,1))
                velocidady=random.choice((-1,1))
                
        ventana.blit(fondo,[0,0])
                #objetos
        if rect1>=0 and rect2<=800:
            medic.rect.x=rect1
   
        medic.rect.y=500
        medicina.rect.x=posicionbolax-20
        medicina.rect.y=posicionbolay-20
        posicionbolax+=velocidadx
        posicionbolay+=velocidady
        if posicionbolax==790:
            velocidadx*= -1
        elif posicionbolax==10:
            velocidadx*= -1
            
        if posicionbolay==590:
            posicionbolay = 300
            life-=1
        elif posicionbolay==10:
            velocidady*= -1
            
        todosObjetos.draw(ventana)
        punto3=pygame.draw.circle(ventana,Blanco,(posicionbolax-20,posicionbolay+20),0)
        punto4=pygame.draw.circle(ventana,Blanco,(posicionbolax+20,posicionbolay+20),0)
        if punto3.colliderect(medic) or punto4.colliderect(medic):
            velocidady*= -1

        if pygame.sprite.spritecollide(medicina, virusLista , True):
            velocidady*= -1
        if life==0 or len(virusLista)==0:
            fluid=False
            
        pygame.display.flip()

    pygame.quit()
    

nivel1()
nivel2()
nivel3()
nivel4()
nivel5()





            

    
