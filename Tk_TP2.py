"""Fait par Jorlive MISSILOU"""

from tkinter import *
from tkinter import ttk, messagebox
import random

main=Tk()
main.geometry("500x400")
main.title("JORLIVE NETWORKING")
largeur, hauteur= 1500, 700
inter=Canvas(main, background="light blue", width=largeur, height=hauteur)
inter.grid()

global env
#lambda event: env.position(event)
class Environnement():
    global env
    def __init__(self):
        # Préparation des images
        self.ppc1= PhotoImage(file="pc1.png") #image de pc
        self.ppc2=PhotoImage(file="pc2.png")
        
        self.psw1=PhotoImage(file="switch1.png") #image de switch
        self.psw2=PhotoImage(file="switch2.png")
        self.psw3=PhotoImage(file="switch3.png")
        
        self.pt1= PhotoImage(file="tel1.png") #image de telephone
        self.pt2= PhotoImage(file="tel2.png")
        
        self.pr1= PhotoImage(file="routeur1.png") #image de routeur
        self.pr2= PhotoImage(file="routeur2.png") 
     
    def imenu(self): # création du menu de l'interface
        self.menubar = Menu(main)
        self.menu_equipement= Menu(self.menubar, tearoff=0)
        self.menu_lien= Menu(self.menubar, tearoff=0)
        
        self.menubar.add_cascade(label="Equipements", menu=self.menu_equipement)
        self.menupc=self.menu_equipement.add_command(label="PC", image=self.ppc1, compound=BOTTOM, command=lambda : env.placement_pc(event)) # ajoute l'élement pc au menu equipement
        self.menu_equipement.add_separator() # Sépare les elements
        
        self.menusw=self.menu_equipement.add_command(label="Switch", image= self.psw1, compound=BOTTOM, command=lambda: env.placement_switch())
        self.menu_equipement.add_separator()
        
        self.menu_equipement.add_command(label="Routeur", image= self.pr1, compound=BOTTOM, command=lambda: env.placement_routeur())
        self.menu_equipement.add_separator()
        
        self.menu_equipement.add_command(label="Téléphone", image= self.pt1, compound=BOTTOM, command=lambda: env.placement_telephone())
        
        self.menubar.add_cascade(label="Aide", command= lambda: env.aide())
        
        self.menubar.add_cascade(label="Fermer", command=main.quit ) 
        main.configure(menu=self.menubar)
        ##########################################################################################
        #######################SWITCH################################
        
    def placement_switch(self):
        self.axe_x= random.randint(5,500) #coordonnées au hasard pour afficher les items sur l'interface
        self.axe_y=random.randint(5,500)  
        self.sw=inter.create_image(self.axe_x, self.axe_y, image=self.psw1, tags="switch")
        self.ns=inter.create_text(self.axe_x, self.axe_y+30, text="switch")
        
        ######################################################################################################""
    def placement_pc(self):
        self.axe_x= random.randint(5,500)
        self.axe_y=random.randint(5,500)  
        self.pc=inter.create_image(self.axe_x, self.axe_y ,image=self.ppc1, tags="pc")
        self.np=inter.create_text(self.axe_x, self.axe_y+30, text="pc")
        #####################################################################################################
    def placement_routeur(self):
        self.axe_x= random.randint(5,500)
        self.axe_y=random.randint(5,500)  
        self.rt=inter.create_image(self.axe_x, self.axe_y ,image=self.pr1, tags="routeur")
        self.nr=inter.create_text(self.axe_x, self.axe_y+30, text="routeur")
        #print(inter.gettags(self.rt))   
        ##########################################################################################################""
    def placement_telephone(self):
        self.axe_x= random.randint(5,500)
        self.axe_y=random.randint(5,500)  
        self.tel=inter.create_image(self.axe_x, self.axe_y ,image=self.pt1, tags="tel")
        self.nt=inter.create_text(self.axe_x, self.axe_y+30, text="telephone")
        #print(inter.gettags(self.tel))
        #################################################################################################################
    def deplacer(self, event):
        self.pres= inter.find_closest(event.x, event.y, halo=7, start= NONE) # sélectionne l'item le plus pres de la souris
        self.tag=inter.gettags(self.pres) # récuperation du tag de l'item en question
        
        # Coordonnées de déplacement
        self.nx= event.x - self.axe_x
        self.ny= event.y - self.axe_y
        self.axe_x= event.x
        self.axe_y= event.y
        
        #Déplacement personnaliser en fonction des tags
        if self.tag== "switch":
            print(self.tag)
            inter.move(self.pres, self.nx, self.ny)
            inter.move(self.ns, self.nx, self.ny+30)
            
        elif self.tag == "pc":
            print(self.tag)

            inter.move(self.pres, self.nx, self.ny)
            inter.move(self.np, self.nx, self.ny+30)
        
        elif self.tag == "routeur":
            print(self.tag)
            inter.move(self.pres, self.nx, self.ny)
            inter.move(self.nr, self.nx, self.ny+30)
            
        else:
            print(self.tag)
            inter.move(self.pres, self.nx, self.ny)
            #inter.move(self.nx, self.ny+30, self.nt)
             
    def suppression(self, event): #suppression des items
        self.proche= inter.find_closest(event.x, event.y)
        inter.delete(self.proche)
     
        #############################LIEN##################################################    
    def position(self, event): # Méthode facilitant la liaison des équipements
        self.recent_x= event.x
        self.recent_y= event.y
        
    """def liaison(self, event):
        inter.create_line((self.recent_x, self.recent_y),(event.x, event.y))
        env.position(event)"""
        
    def lien(self, event): # lien des équipements
        #env.position(event)
        self.cable=inter.create_line((self.recent_x, self.recent_y,event.x, event.y))
        #############################################################################################
    
    """def menu_modif(self):
        self.chmenu=Menu(main, tearoff=0)
        self.chmenu.add_command(label="Lien (Câble)")
        self.chmenu.add_command(label="Changer le nom")
        self.chmenu.add_command(label="Changer d'icône (image)", command= lambda event: env.changement(event))
        self.chmenu.add_command(label="supprimer", command= lambda event: Environnement.suppression(event))"""

    """def modif_topup(self, event):
        self.chmenu.tk_popup(event.x_root, event.y_root)"""
        
        
    def changement(self, event):
        self.icon= inter.find_closest(event.x, event.y)
        self.icon_tag= inter.gettags(self.icon)
        #print(self.icon_tag)
        
        if "switch" in self.icon_tag:
            inter.itemconfigure(self.icon, image= self.psw2)
            
        elif "pc" in self.icon_tag:
            inter.itemconfigure(self.icon, image= self.ppc2)
            
        elif "tel" in self.icon_tag:
            inter.itemconfigure(self.icon, image= self.pt2)
        
        if "routeur" in self.icon_tag:
            inter.itemconfigure(self.icon, image= self.pr2)
    #############################################################################"#############################    
    def aide(self): # affiche le mode d'emploi de l'application
        messagebox.showinfo("Mode d'emploi", """S: afficher un switch \n P: afficher un pc \n R: afficher un routeur \n T: afficher un téléphone \n \n Déplacement: faire glisser un équipement pour le déplacer \n
                    \n Lien: pour relier des équipements, faire un clic gauche sur un point puis placer la souris sur l'autre point
                    et appuyer sur *L* \n \n Click droit: pour supprimer un équipement
                    \n \n C: pour changer l'icone d'un équipement """)
           
env=Environnement() #instanciation de la classe
env.imenu()
#env.menu_modif()
lambda event: env.position(event)

main.bind_all("<B1-Motion>", lambda event: env.deplacer(event)) # Déplacement
main.bind_all("<Button-1>", lambda event:env.position(event))
main.bind_all("<Button-3>", lambda event: env.suppression(event))

#              Raccourcis
main.bind_all("<KeyPress-s>", lambda k: env.placement_switch())
main.bind_all("<KeyPress-r>", lambda k: env.placement_routeur())
main.bind_all("<KeyPress-p>", lambda k: env.placement_pc())
main.bind_all("<KeyPress-t>", lambda k: env.placement_telephone())
main.bind_all("<KeyPress-l>", lambda event:env.lien(event))
main.bind_all("<KeyPress-c>", lambda event:env.changement(event))

main.mainloop()