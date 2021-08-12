from enumerations import Resource

class BoardConfigurations():

    beginner_resource_order = [
        [Resource.LUMBER, Resource.WOOL, Resource.GRAIN],
        [Resource.BRICK, Resource.ORE, Resource.BRICK, Resource.GRAIN],
        [Resource.NONE, Resource.LUMBER, Resource.GRAIN, Resource.LUMBER, Resource.GRAIN],
        [Resource.BRICK, Resource.WOOL, Resource.WOOL, Resource.ORE],
        [Resource.ORE, Resource.GRAIN, Resource.LUMBER]
    ]

    beginner_num_tokens_order = [
        [11, 12, 9],
        [4, 6, 5, 10],
        [None, 3, 11, 4, 8],
        [8, 10, 9, 3],
        [5, 2, 6],
    ]