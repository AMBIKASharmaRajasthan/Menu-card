#!/usr/bin/env python
# coding: utf-8

# In[1]:


class cafe:
    def __init__(self):
        print("Ambika Cafe")
        print("Since 1999")
        print("www.ambikacafe.com")
        print("Menu\n")
        l=["Indian","French","Italian"]
        for k in l:
            print(k)
            
    def indian(self):
        import pandas as pd
        indian={"Food_Name":["DalBati","Samosa","Dosha","Jalibi","Lassi"],"Price":[150,18,80,160,30]}
        df=pd.DataFrame(indian)
        print(df)
        l=[]
        x=True
        while x:
            a=int(input("Enter the Food name ID:"))
            b=int(input("Enter the quantity:"))
            price=df["Price"][a]
            d=price*b
            l.append(d)
            x=input("Do you want to re-order !")
            if x=="no":
                break
                print("Thank You")
                
        t=sum(l)
        s=t*0.18
        total=t+s
        print("Total Price : ",total)
        print("Tax Included : ","18%")
        print("Thank u! Visit Again")
        


# In[2]:


obj=cafe()


# In[4]:


y=input("Enter the food type:")
if y=="Indian":
    obj.indian()


# In[ ]:





# In[ ]:


class cafe:
    def __init__(self):
        print("Ambika Cafe")
        print("Since 1999")
        print("www.ambikacafe.com")
        print("Menu\n")
        l=["Indian","French","Italian"]
        for k in l:
            print(k)


# In[ ]:


obj=cafe()


# In[ ]:





# In[1]:


class cafe:
    def _init_(self):
        print("Ambika Cafe")
        print("Since 1999")
        print("www.ambikacafe.com")
        print("Menu\n")
        l=["Indian","French","Italian"]
        for k in l:
            print(k)
        
                
    def french(self):
        import pandas as pd
        french={"Food_Name":["chocolate souffle","Eclair","Crepe","Macaron","The croissant"],"Price":[200,150,180,460,530]}
        df=pd.DataFrame(french)
        print(df)
        l=[]
        x=True
        while x:
            a=int(input("Enter the Food name ID:"))
            b=int(input("Enter the quantity:"))
            price=df["Price"][a]
            d=price*b
            l.append(d)
            x=input("Do you want to re-order !")
            if x=="no":
                break
                print("Thank You")
                
        t=sum(l)
        s=t*0.18
        total=t+s
        print("Total Price : ",total)
        print("Tax Included : ","27%")
        print("Thank u! Visit Again")


# In[2]:


obj=cafe()


# In[3]:


r=input("Enter the food type:")
if r=="french":
    obj.french()


# In[4]:


class cafe:
   def _init_(self):
       print("Ambika Cafe")
       print("Since 1999")
       print("www.ambikacafe.com")
       print("Menu\n")
       l=["Indian","French","Italian"]
       for k in l:
           print(k)
       
               
   def italian(self):
       import pandas as pd
       french={"Food_Name":["Pizza","lasagna","Tiramisu","Caprese","Risotto"],"Price":[200,150,180,460,530]}
       df=pd.DataFrame(french)
       print(df)
       l=[]
       x=True
       while x:
           a=int(input("Enter the Food name ID:"))
           b=int(input("Enter the quantity:"))
           price=df["Price"][a]
           d=price*b
           l.append(d)
           x=input("Do you want to re-order !")
           if x=="no":
               break
               print("Thank You")
               
       t=sum(l)
       s=t*0.18
       total=t+s
       print("Total Price : ",total)
       print("Tax Included : ","27%")
       print("Thank u! Visit Again")


# In[5]:


obj=cafe()


# In[8]:


r=input("Enter the food type:")
if r=="italian":
    obj.italian()


# In[ ]:





# In[ ]:




