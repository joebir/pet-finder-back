import models


from flask import Blueprint, jsonify, request
from flask_login import current_user
from playhouse.shortcuts import model_to_dict


pet = Blueprint('pets', 'pet')


@pet.route('/', methods=['get'])
def get_all_pets():
    try:
        pets = [model_to_dict(pet) for pet in current_user.pets]
        print(f"here is the list of pets. {pets}")
        return jsonify(data=pets, status={"code": 201, "message": "success"})

    except models.DoesNotExist:
        return jsonify(
        data={}, status={"code": 401, "message": "Error getting Resources"})


@pet.route('/', methods=["POST"])
def create_pets():
    payload = request.get_json()
    print(type(payload), 'payload')
    pet = models.Pet.create(
    petName=payload['petName'],
    aboutPet=payload['aboutPet'],
    dateLost=payload['dateLost'],
    reunited=payload['reunited'],
    user=current_user.id,
    photo=payload['photo'],
    status=payload['status'])

    print(pet.__dict__)
    print(dir(pet))
    print(model_to_dict(pet), 'model to dict')
    pet_dict = model_to_dict(pet)
    return jsonify(data=pet_dict, status={"code": 201, "message": "Success"})


@pet.route('/<id>', methods=["GET"])
def get_one_pet(id):
    dog = models.pet.get_by_id(id)
    return jsonify(data=model_to_dict(pet), status={"code": 200, "message": "Success"})


@pet.route('/<id>', methods=["PUT"])
def update_pet(id):
    payload = request.get_json()
    query = models.Pet.update(**payload).where(models.Pet.id==id)
    query.execute()
    dog = model_to_dict(models.Pet.get_by_id(id))
    return jsonify(data=pet, status={"code": 200, "message": "Success"})


@pet.route('/<id>', methods=["DELETE"])
def delete_pet(id):
    delete_query = models.Pet.delete().where(models.Pet.id == id)
    num_of_rows_deleted = delete_query.execute()
    return jsonify(
    data={},
    message="{} Woof Woof Meow Meow went home. Pet with id {}".format(num_of_rows_deleted, id),
    status={"code": 200}
    )


# end
