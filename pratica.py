my_family = []
select = 0
index = 0
name_new_member = ""

def add_member(name_new_member):
    my_family.append(name_new_member)
    print(f"Boas vindas a {my_family[-1]}")

def edit_member(index, name_member):
    new_name_member = input(f"Digite o novo nome de {name_member}: ")
    my_family[index] = new_name_member
    print(f"o nome de {my_family[index]} foi alterado com sucesso")

def delete_member(name_member):
    my_family.remove(name_member)
    print(f"{name_member} foi excluido com sucesso!")

def print_members():
    index = 0
    for member in my_family:
        print(f"{index+1} - {member}")

while True:
    select = int(input("Programa da família\n1 - Novo Membro\n2 - Editar Membro\n3 - Excluir Membro\n4 - Imprimir Membros\n0 - Sair\nO que deseja? "))
    match select:
        case 0:
            exit()
        case 1:
            name_new_member = input("Digite o nome do novo membro da família: ")
            name_new_member.lower()
            if(name_new_member not in my_family):
                add_member(name_new_member)
            else:
                print(f"{name_new_member} já faz parte da família!")
        case 2:
            name_member = input("Digite o nome do membro da família que deseja editar: ")
            name_member.lower()
            if(name_member in my_family):
                index = my_family.index(name_member)
                edit_member(index, name_member)
            else:
                print(f"Membro não encontrado!")
        case 3:
            name_member = input("Qual o nome do membro que deseja excluir? ")
            name_member.lower()
            if(name_member in my_family):
                delete_member(name_member)
            else:
                print(f"Membro não encontrado!\n")
        case 4:
            print_members()