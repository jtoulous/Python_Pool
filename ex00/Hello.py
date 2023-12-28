ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


#list_modif
ft_list[1] = "World!"

#tuple_modif
tmpTuple = ("Hello", "France!")
ft_tuple = tmpTuple

#set_modif
ft_set.discard("tutu!")
ft_set.add("Paris!")

#dict_modif
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
