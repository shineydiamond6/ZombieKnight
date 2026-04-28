import pygame


class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=None):
        """Initialize the tile"""
        super().__init__()

        # TODO: assign pygame.transform.scale() to self.image.  The scale() function call gets the following are arguments
        # pygame.image.load(f"images/tiles/Tile ({image_int}).png")
        # (32, 32)

        # TODO: if sub_group is not None:
            # TODO: call sub_group.add() passing in self as the argument
        # TODO: call main_group.add() passing in self as the argument.

        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign (x, y) to self.rect.topleft
        # TODO: assign pygame.mask.from_surface() to self.mask  The from_surface() function call gets self.image as its argument

