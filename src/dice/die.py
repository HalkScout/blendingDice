import bpy

from abc import ABC, abstractmethod
from util.text_utils import create_numbers

class Die(ABC):
    def __init__(self, name, scale=1, offset=0):
        self.name = name
        self.scale = scale
        self.offset = offset

    def create(self):
        collection = bpy.data.collections.new(self.name)
        bpy.context.scene.collection.children.link(collection)
        obj = self.create_mesh(collection)
        create_numbers(obj, collection, self.scale, self.numbers)

    @abstractmethod
    def create_mesh(self, collection):
        raise RuntimeError("Subclass does not implement 'create_mesh'.")