var_test = " " 
fix_var_test = var_test.strip()
print(f"len var_test is {len(fix_var_test)}")
print(f"var_test is null : {fix_var_test is None}")

list_test = ['2015',]
print(f"len list_test is {len(list_test)}")


lst_test = 'TALEND, SSIS, POWERBI, TABLEAU, CLICKVIEW'
viz = lst_test.split()[-3]
print("Les valeurs liées à la viz sont : {viz}")