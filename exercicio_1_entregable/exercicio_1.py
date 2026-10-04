from faker import Faker
import random

fake = Faker()
usuarios = []
contador_usuarios = 0


while contador_usuarios < 15:
    id = contador_usuarios + 1
    usuario = {
        "id" : id,
        "nome": fake.name(),
        "direccion": fake.address(),
        "correo_electronico": fake.email(),
        "telefono": fake.phone_number()
    }

    usuarios.append(usuario)
    contador_usuarios +=1

print(usuarios)

usuario_seleccionado = random.choice(usuarios)
print(f"O usuario chamado {usuario_seleccionado['nome']} foi o afortunado!")

