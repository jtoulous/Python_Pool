from find_ft_type import all_thing_is_obj

ft_list = ["ta", "mere"]
ft_tuple = ("ta", "soeur")
ft_dict = {"ta" : "grand-mere"}
ft_set = {"ta", "cousine"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))