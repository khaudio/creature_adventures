# Creature Adventures

Battle using `Creatures`, collect `Items` to build `Artifacts`, win `Sigils` in battle, then claim victory in `The Colosseum`, and dethrone the Emperor.
Traverse the game board and roll to determine the outcome of each encounter.

# Gameplay

Players take turns moving around the board and engaging in battles.  Roll to see who goes first.  All players start at their respective home.

Roll to move the specified number of spaces on the board.  When crossing through or landing on `Wilderness` tiles, add one `Footstep Counter` per wilderness tile crossed that turn, minus any counters reduced if the player has `Quiet Shoes`.  When the player completes movement, roll for a wild creature encounter (see `The Wilderness`).

If a player's movement ends on a special tile, begin an encounter with that game element.  If movement ends on the same tile as another player, initiate combat with that player.

## Winning

There are multiple avenues to victory.

### **Domination**

One path is to become the hero of `The Colosseum`.  To win, a player must collect all three `Sigils` and subsequently defeat all consecutive battles in `The Colosseum`.

### **Collector**

Another way to win is to catch a total of 15 creatures.  Although no one may hold more than three creatures at a time, if a player successfully catches 15 creatures throughout the game, that player becomes `Creature Master`, ending the game.

### **Survivalist**

When the creature deck is empty, players may duel in sudden death.  All `Sigils` become inactive.  The victor of each duel may collect creatures from the defeated player as they are removed from play.  The last player standing wins.

# Creatures

Creatures do battle by attacking and defending.  When a creature's `HP` falls to zero, the creature is unable to battle until revived at `Home` or by a `Shaman`.

There are multiple tiers of creatures, and some have unique abilites.

Creatures have three attributes: `HP`, `Attack`, and `Defense`.

## **HP**

Hit points available for each creature.  Each creature has a maximum `HP` value.  When a creature's `HP` reaches zero, it is unavailable during battle and must be revived.

## **Attack**

The physical damage a creature does to another creature's HP in battle.  Physical damage is negated by the defending creature's `Defense` value.  All other damage types ignore defense and do damage to HP directly.

## **Defense**

The base defense value used to mitigate physical damage done by the aggressor's `Attack` value; i.e., if a creature strikes for 4 damage, and the defender's `Defense` is 3, it will sustain 1 damage to its `HP` when attacked.  Defense value does not protect against poison or other non-physical damage.

## **Wild Creatures**

Wild creatures are encountered when crossing `Wilderness` tiles on the game board.  They can be defeated or caught.

When a creature is caught, a player can choose to either discard the new creature, or keep it to replace one of the three in their hand.


# Combat

In addition to basic combat abilities, creatures may have individual combat abilities.

## **Player vs Player**

In battles, players take turns choosing offensive or defensive moves.  The player who initiates a battle attacks first, unless the defender has the `Sigil of Speed`.

Only one creature can be used at a time.  Each player chooses which creature to use when the battle begins.

Combat actions include:

- **Attack**
    - `Strike` (Roll 1d6 for chances of inflicting physical damage)
        - 1     Attack misses
        - 2     Counterstrike: Both creatures strike each other for physical damage
        - 3-5   Attack lands
        - 6     Critical hit for double damage
    - `Meditate` (Roll to increase `Attack` until the end of next volley)
        - 1     No change to attack
        - 2-5   Raise `Attack` by 2 points
        - 6     `Attack` doubles

- **Defend**
    - `Brace` (Roll to boost `Defense` until the end of next volley)
        - 1     No change to `Defense`
        - 2-5   Raise `Defense` by 2 points
        - 6     `Defense` doubles
    
    - `Dodge` (Roll to dodge current opponent attack entirely)
        - 1-4   Dodge is unsuccessful
        - 5     Dodge is successful
        - 6     Parry: Dodge attack and counterstrike opponent for physical damage

    - `Inner Peace` (Heal a pre-assigned creature for 50% HP if the player has the `Sigil of Wisdom`).  `Inner Peace` may not be used to revive a creature while in battle.

- **Switch**
    - Switch to another creature

- **Forfeit**
    - Admit defeat and return `Home`.  Any `Sigils` go to the victor.

## **Single Player Combat**

Single player combat differs somewhat from PvP.  Offensive moves are still available, but the possible outcomes change.

- **Attack**
    - `Strike` (Roll for chances of inflicting damage)
        - 10% chance for a miss (No damage done)
        - 40% chance for an unmitigated hit (Attacking creature's base `Attack` power)
        - 40% chance to receive a counterstrike (NPC `Attack` power damage done to player)
        - 10% chance for a critical hit (Double `Attack` power)

    - `Meditate` (Roll to increase `Attack` for current and next turn)
        - 50% chance to receive an interrupting hit from opponent
        - 30% chance to raise `Attack` by 50%
        - 20% chance to raise `Attack` by 100%

- **Defend**
    - `Inner Peace` (Heal a pre-assigned creature for 50% HP if the player has the `Sigil of Wisdom`).  `Inner Peace` may not be used to revive a creature while in battle.

- **Switch**
    - Switch to another creature

- **Escape**
    - Roll to escape a wild creature encounter.
        - 50% chance the player escapes
        - 50% chance the player is trapped and must proceed to the next turn of combat

- **Forfeit**
    - Admit defeat and return `Home`.  Any `Sigils` held return to `Warlords`.


# Shaman

`Shaman` revive and heal creatures by variable amounts.

Choose a creature to heal and roll 1d6 for the amount of HP healed.

# Sigils

`Sigils` are obtained by defeating Warlords or other players who currently possess sigils.  There are three total sigils, and a player must have all three to enter The Colosseum to complete the game.  When one player loses to another, they must forfeit all sigils they currently posses.  When one player attacks another, the aggressor is afflicted by `Exhaustion`, losing the following turn.  If the defending player is victorious, they are bolstered by `Rally Cry`, and all three creatures' HP is doubled for one turn and healed fully.

For example, if Player A attacks Player B unsuccessfully, Player A returns `Home` with `Exhaustion`, and Player B gains `Rally Cry` that lasts through Player B's next turn, as it was Player A's turn when the attack took place.

## **Sigil of Power**

The `Sigil of Power` gives three temporary `Attack` points to the player who holds it that can be redistributed at will once per turn, if desired.

## **Sigil of Speed**

The `Sigil of Speed` allows a player to attack first in battle.  Essentially, the player with this `Sigil` receives one free hit to open the battle.  Afterward, battle continues normally (simultaneous actions).

## **Sigil of Wisdom**

The `Sigil of Wisdom` assigns an additional defensive ability called `Inner Peace` to a single creature that may be re-assigned once per turn.  `Inner Peace` heals the creature for 50% HP and can be used once per turn, either in or out of battle.  If `Inner Peace` is used to revive a creature with zero HP, it may only be used out of battle.


# Places

## **Home**

The starting place of the game, and where players return to when all a player's creatures' `HP` is depleted.  A player may also choose to rest at `Home` to forego their next turn and fully heal all creatures.

## **The Wilderness**

The Wilderness is comprised of all pieces of the game board that are covered in foliage.  Every time a wilderness tile is crossed by a player, add one footstep counter.  At the end of a player's movement, roll to discover whether a wild creature battle occurs.  The player must roll higher than the number of footstep counters to avoid a battle.

For example, if a player moves across 3 wilderness tiles in a turn, they must roll 4 or higher to avoid a wild creature encounter.

## **Thieves**

Thieves are combatants found among The Wilderness that award extra 

## **Warlords**

`Warlords` are found around the map and must be battled to receive `Sigils`.  Each warlord defeated yields one sigil.  `Warlords` do not scale with player level.

## **The Colosseum**

`The Colosseum` is a gauntlet of three consecutive battles that may only be performed once a player holds all three `Sigils`.  Each battle takes one turn.  Regular play resumes for other players between each battle.  Once one player start combat in `The Colosseum`, all other players gain `Vigilance` and may attack the player participating in the gauntlet.  If an attacker succeeds, that player receives the required `Sigils`, restarts `The Colosseum` as the active combatant, and loses `Vigilance`, while the defeated player gains it after being sent `Home`.  Once three single-player battles in a row have been won, that player usurps the throne, and the game ends.

# Artifacts

`Artifacts` are game modifiers that are less powerful than `Sigils` and are not required for victory.  Artifacts can be purchased using materials.  All players can purchase all items; i.e., unlike `Sigils`, there is no limit to the number of `Artifacts` a player may have.

## **Fortify**

`Fortify` allows a player to begin defensive combat with `Brace`, even if the opponent has the `Sigil of Speed`.

## **Tailwind**

`Tailwind` allows the player to roll twice for movement.  Only one roll may be used to move across the board; i.e., if a player rolls a 2 and then 6, they may choose to move 6 spaces, discarding the roll of 2.

## **Ascension**

`Ascension` swaps any two players' positions on the game board.  It can only be used once per charge; i.e., once a player uses `Ascension`, they must purchase another one using more `Attribute Points`.  Furthermore, the player receives `Astral Sickness` after casting, and cannot use `Ascension` on the next turn.

## **Quiet Shoes**

`Quiet Shoes` slows the accumulation of foostep counters in the wilderness.

- Level 1 (Cost: 1 `Attribute Point`):

    Accumulate one less counter per turn when walking through wilderness

- Level 2 (Cost: 2 `Attribute Points`):

    Accumulate two less counters per turn when walking through wilderness

- Level 3 (Cost: 3 `Attribute Points`):

    Accumulate three less counters per turn when walking through wilderness

## **Infinite Bandage**

`Infinite Bandage` allows the players creatures to heal at the end of each turn without visiting a Shaman or Home.

- Level 1 (Cost: 1 Attribute Point)

    Heal all creatures by 5% at the end of each turn

- Level 2 (Cost: 2 `Attribute Points`)

    Heal all creatures by 10% at the end of each turn

- Level 3 (Cost: 5 `Attribute Points`)

    Heal all creatures by 20% at the end of each turn


# Conditions and Curses

## Vigilance

When on player begins the combat tournament in `The Colosseum`, all other players gain `Vigilance`, raising `Attack` and `Defense` by 20% while `The Colosseum` is active.

## **Exhaustion**

A player is afflicted by `Exhaustion` after attacking another player and must lose the following turn to recover.

## **Rally Cry**

A player gains `Rally Cry` after successfully defending against an attack from another player.  All three creatures' maximum `HP` is doubled and fully healed.  After `Rally Cry` wears off, creatures' maximum `HP` returns to normal, and any excess `HP` is lost.

## **Astral Sickness**

A player becomes ill with `Astral Sickness` after using `Ascension`.  The player may not use `Ascension` for one turn.

