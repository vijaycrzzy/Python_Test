sam_dict=[{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
                                                                                                                    
sam_dict.sort(key=lambda c: int(c['model']), reverse=True) # type: ignore[index]

print(sam_dict)

