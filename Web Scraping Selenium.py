

# In[1]:


import selenium
from selenium import webdriver 
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver=webdriver.Chrome(r"")


# In[3]:


url = "https://www.myntra.com/shoes"
driver.get(url)


# In[4]:


price_filter=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div")
price_filter.click()


# In[5]:


col_filter=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[6]/ul/li[1]/label/div")
col_filter.click()


# In[6]:


#Extracting Product Brand
brand_name=driver.find_elements_by_xpath("//h3[@class='product-brand']")
len(brand_name)


# In[7]:


brand_name


# In[8]:


brand=[]
for i in brand_name:
   brand.append(i.text)
len(brand)  
brand


# In[9]:


#Extracting Product Description
brand_descp=driver.find_elements_by_xpath("//h4[@class='product-product']")
len(brand_descp)


# In[10]:


brand_descp


# In[11]:


Description=[]
for i in brand_descp:
   Description.append(i.text)
len(Description)  
Description


# In[12]:


#Extracting Product Price
brand_price=driver.find_elements_by_xpath("//div[@class='product-price']")
len(brand_price)


# In[13]:


brand_price


# In[14]:


Price=[]
for i in brand_price:
   Price.append(i.text)
len(Price)  
Price


# In[15]:


sneakers_1=pd.DataFrame()
sneakers_1['Brand_name']=brand
sneakers_1['Brand_Description']=Description
sneakers_1['Brand_Price']=Price
sneakers_1






