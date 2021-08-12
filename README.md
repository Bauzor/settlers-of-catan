# Notes for implementation of Settlers of Catan
hexes are always indexed from the top left corner as 0 (edge or vertex)
then counted clockwise

# Class handles what
- board creation
    - hex creation
    - vertices creation and sharing
    - port creation
- validation of piece placement relative to other board elements
    - settlements two roads away
    - cities replace settlments
    - roads connected to settlement or other roads
- 