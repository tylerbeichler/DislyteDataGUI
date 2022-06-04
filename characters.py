

class Character:
    def __init__(self, char_data):
        """
        :param char_data: {
                'rarity': int,                              // 3, 4, 5
                'name': string,                             // 'character name'
                'class': string,                            // 'fighter', 'support', 'defender', 'controller'
                'elemental_class': string,                  // 'inferno', 'wind', 'flow', 'shimmer'
                'captain_ability': string,                  // 'ability description'
                'abilities': {string: string,...},          // {'ability_name_0': 'description_0',...}
                'recommended_relics': (string, string)[],   // [('set_name', 'set_name'),...]
                'base_stats': {string: int,...},            // {'stat_0': 123,...}
                'max_stats': {string: int,...}              // {'stat_0': 123,...}
                }
        """
        self.data = char_data

