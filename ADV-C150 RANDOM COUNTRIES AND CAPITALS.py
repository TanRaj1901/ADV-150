from tkinter import *
import random

root=Tk()

root.title("Random City Generator")
root.geometry("500x500")

country_input=Entry(root)
country_input.place(relx=0.5,rely=0.2,anchor=CENTER)
capital_input=Entry(root)
capital_input.place(relx=0.5,rely=0.3,anchor=CENTER)

label_country=Label(root)
label_capital=Label(root)
label_ran_country=Label(root)
label_ran_capital=_city=Label(root)

capital_list=[]
country_list=[]

def adding_country_capital():
    country_name=country_input.get()
    country_list.append(country_name)
    label_country["text"]= "Country Name: " + str(country_list)
    
    capital_name=capital_input.get()
    capital_list.append(capital_name)
    label_capital["text"]= "Capital Name: " + str(capital_list)
def random_capital_country():
    country_length= len(country_list)
    random_country = random.randint(0,country_length)
    country_ran= country_list[random_country]
    label_ran_country["text"] = "Random Country: "+str(country_ran)
    
    capital_length= len(capital_list)
    random_capital = random.randint(0,capital_length)
    capital_ran= capital_list[random_capital]
    label_ran_capital["text"] = "Random Capital: "+str(capital_ran)
    
btn=Button(root,text=" Display Country And City Name" ,command=adding_country_capital)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

btn1=Button(root,text="Display Country And City Name Randomly",command=random_capital_country)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)

label_country.place(relx=0.5,rely=0.5,anchor=CENTER)
label_capital.place(relx=0.5,rely=0.6,anchor=CENTER)
label_ran_country.place(relx=0.5,rely=0.8,anchor=CENTER)
label_ran_capital.place(relx=0.5,rely=0.9,anchor=CENTER)



root.mainloop()