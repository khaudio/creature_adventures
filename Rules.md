# Creature Adventures

Battle using `Creatures`, collect `Sigils`, gain `Attributes` and `Artifacts`, then claim victory in `The Colosseum`, and dethrone the Emperor to win.
Traverse the game board and roll to determine the outcome of each encounter.


# Gameplay

Players take turns moving around the board and engaging in battles.  Roll to see who goes first.  All players start at their respective home.

Roll to move the specified number of spaces on the board.  When crossing through or landing on `Wilderness` tiles, add one `Footstep Counter` per wilderness tile crossed that turn, minus any counters reduced if the player has `Quiet Shoes`.  When the player completes movement, roll for a wild creature encounter (see `The Wilderness`).

If a player's movement ends on a special tile, begin an encounter with that game element.  If movement ends on the same tile as another player, initiate combat with that player, unless on a special tile (`Home`, `Shaman`, `Warlord`, or `Thieves`).

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

## **Attribute Points**

Creatures have three attributes: `HP`, `Attack`, and `Defense`.  Once assigned, attributes cannot be reassigned, with the exception of the three temporary points provided by the `Sigil of Power`.


### **HP**

Hit points available for each creature.  Each creature has a maximum `HP` value.  When a creature's `HP` reaches zero, it is unavailable during battle and must be revived.  All creatures begin the game with 10 `HP`.  Assigning an `Attribute Point` raises the maximum `HP` by 2.

### **Attack**

The base damage a creature does to another creature's HP in battle.

### **Defense**

The base defense value used to mitigate damage done by the aggressor's `Attack` value; i.e., if a creature strikes for 4 damage, and the defender's `Defense` is 3, it will sustain 1 damage to its `HP` when the attack is deflected.

## **Wild Creatures**

Wild creatures are encountered when crossing `Wilderness` tiles on the game board.  They can be defeated or caught.  Catching a wild creature awards 2 EXP points, while defeating it yields a single EXP point.

When a creature is caught, a player can choose to either discard the new creature, or keep it to replace one of the three in their hand.  `Attribute Points` from the discarded creature are lost and do not transfer (except for those granted by the `Sigil of Power`).


# Levels and EXP

All players begin the game at level 1.  Whenever a creature is defeated in battle, players gain 1 EXP.  When enough EXP is gained, players gain a level.  Maximum level is 5.  Each time a level is gained, players are awarded `Attribute Points` that can be assigned to any creature or traded for `Artifacts`.  EXP is awarded following all victorious battles, including ones with wild creatures.  The maximum `Attribute Points` that a player can earn is 15.

- Level 1

    1 `Attribute Point` given to players to begin game

- Level 2 (Requires 3 EXP at Level 1)

    2 `Attribute Points` earned

- Level 3 (Requires 4 EXP at Level 2)

    3 `Attribute Points` earned

- Level 4 (Requires 6 EXP at Level 3)

    4 `Attribute Points` earned

- Level 5 (Requires 8 EXP at Level 4)

    5 `Attribute Points` earned

# Combat

In addition to basic combat abilities, creatures may have individual combat abilities.

## **Player vs Player**

In battles, players take turns choosing offensive or defensive moves.  The player who initiates a battle attacks first, unless the defender has the `Sigil of Speed`.

Only one creature can be used at a time.  Each player chooses which creature to use when the battle begins.

Combat actions include:

- **Attack**
    - `Strike` (Roll for chances of inflicting damage)
        - 10% chance for a miss (No damage done)
        - 20% chance for an unmitigated hit (Attacking creature's base `Attack` power)
        - 50% chance for a deflected hit (Attacker's `Attack` power minus defender's `Defense`)
        - 10% chance to receive a counterstrike ('Attack' power compared and creature with less takes difference as damage)
        - 10% chance for a critical hit (Double `Attack` power minus defender's `Defense`)
    - `Meditate` (Roll to increase `Attack` for one turn)
        - 10% chance for no change to `Attack`
        - 50% chance to raise `Attack` by 20%
        - 30% chance to raise `Attack` by 40%
        - 10% chance to raise `Attack` by 100%

- **Defend**
    - `Brace` (Roll to boost `Defense` for one turn)
        - 10% chance for no change to `Defense`
        - 50% chance to raise `Defense` by 20%
        - 30% chance to raise `Defense` by 40%
        - 10% chance to raise `Defense` by 100%
    - `Dodge` (Roll to dodge attack entirely)
        - 60% chance dodge is unsuccessful
        - 40% chance attack is dodged (No damage done)
    - `Inner Peace` (Heal a pre-assigned creature for 50% HP if the player has the `Sigil of Wisdom`).  `Inner Peace` may not be used to revive a creature while in battle.

- **Switch**
    - Switch to another creature

- **Forfeit**
    - Admit defeat and return `Home`.  Any `Sigils` go to the victor.

## **Single Player Combat**

Single player combat is somewhat different than with PvP.  Offensive moves are still available, but the possible outcomes change.

- **Attack**
    - `Strike` (Roll for chances of inflicting damage)
        - 10% chance for a miss (No damage done)
        - 40% chance for an unmitigated hit (Attacking creature's base `Attack` power)
        - 40% chance to receive a counterstrike (NPC `Attack` power damage done to player)
        - 10% chance for a critical hit (Double `Attack` power)

    - `Meditate` (Roll to increase `Attack` for one turn)
        - 10% chance for no change to `Attack`
        - 50% chance to raise `Attack` by 20%
        - 30% chance to raise `Attack` by 40%
        - 10% chance to raise `Attack` by 100%

- **Defend**
    - `Inner Peace` (Heal a pre-assigned creature for 50% HP if the player has the `Sigil of Wisdom`).  `Inner Peace` may not be used to revive a creature while in battle.

- **Switch**
    - Switch to another creature

- **Run**
    - Roll to escape a wild creature encounter.
        - 50% chance the player escapes
        - 50% chance the player is trapped and must proceed to the next turn of combat

- **Forfeit**
    - Admit defeat and return `Home`.  Any `Sigils` held return to `Warlords`.


# Shaman

`Shaman` revive and heal creatures by variable amounts.  Players can choose how much to risk when rolling for healing.

Choose:

- 50% healing to one creature without rolling
- Roll for a chance to heal one creature
    - 50% chance for 25% healing
    - 30% chance for 75% healing
    - 20% chance for 100% healing
- Roll for a chance to heal all creatures
    - 50% chance for 0% healing
    - 30% chance for 10% healing
    - 20% chance for 100% healing


# Sigils

`Sigils` are obtained by defeating Warlords or other players who currently possess sigils.  There are three total sigils, and a player must have all three to enter The Colosseum to complete the game.  When one player loses to another, they must forfeit all sigils they currently posses.  When one player attacks another, the aggressor is afflicted by `Exhaustion`, losing the following turn.  If the defending player is victorious, they are bolstered by `Rally Cry`, and all three creatures' HP is doubled for one turn and healed fully.

For example, if Player A attacks Player B unsuccessfully, Player A returns `Home` with `Exhaustion`, and Player B gains `Rally Cry` that lasts through Player B's next turn, as it was Player A's turn when the attack took place.

## **Sigil of Power**

The `Sigil of Power` gives three temporary `Attribute Points` to the player who holds it that can be redistributed at will once per turn, if desired; however, if the creature's HP is empty, points gained by `Sigils` may not be added or removed until the creature is revived.

For example, a player may add three `Attack` points to a single creature, and on the next turn, move two of those three points to another creature's `Defense`.

## **Sigil of Speed**

The `Sigil of Speed` allows a player to attack first.  If defending, the player may strike first.  If attacking, the player with the sigil may execute two attacks in a row before the defending player may respond.

## **Sigil of Wisdom**

The `Sigil of Wisdom` assigns an additional defensive ability called `Inner Peace` to a single creature that may be re-assigned once per turn.  `Inner Peace` heals the creature for 50% HP and can be used once per turn, either in or out of battle.  If `Inner Peace` is used to revive a creature with zero HP, it may only be used out of battle.


# Places

## **Home**

The starting place of the game, and where players return to when all a player's creatures' `HP` is depleted.  A player may also choose to rest at `Home` to forego their next turn and fully heal all creatures.

## **The Wilderness**

The Wilderness is comprised of all pieces of the game board that are covered in foliage.  Every time a wilderness tile is crossed by a player, add one footstep counter.  At the end of a player's movement, roll to discover whether a wild creature battle occurs.  The player must roll higher than the number of footstep counters to avoid a battle.

For example, if a player moves across 3 wilderness tiles in a turn, they must roll 4 or higher to avoid a wild creature encounter.

## **Thieves**

Thieves are combatants found among The Wilderness that provide extra EXP if defeated, at the risk of losing `Attribute Points`.  Players may choose to gamble up to three `Attribute Points` and roll to decide the number of battles required.  Thieves scale with player level.

- 50% chance to battle one creature
- 30% chance to battle two creatures
- 20% chance to battle three creatures

## **Warlords**

`Warlords` are found around the map and must be battled to receive `Sigils`.  Each warlord defeated yields one sigil.  `Warlords` do not scale with player level.

## **The Colosseum**

`The Colosseum` is a gauntlet of three consecutive battles that may only be performed once a player holds all three `Sigils`.  Each battle takes one turn.  Regular play resumes for other players between each battle.  Once one player start combat in `The Colosseum`, all other players gain `Vigilance` and may attack the player participating in the gauntlet.  If an attacker succeeds, that player receives the required `Sigils`, restarts `The Colosseum` as the active combatant, and loses `Vigilance`, while the defeated player gains it after being sent `Home`.  Once three single-player battles in a row have been won, that player usurps the throne, and the game ends.

# Artifacts

`Artifacts` are game modifiers that are less powerful than `Sigils` and are not required for victory.  Artifacts can be purchased using `Attribute Points`.  All players can purchase all items; i.e., unlike `Sigils`, the number of available `Artifacts` is not finite.

## **Fortify**

`Fortify` allows a player to begin defensive combat with `Brace`, even if the opponent has the `Sigil of Speed`.

- Level 1 (Cost: 1 `Attribute Points`)

    Roll to `Brace` before the first attack

- Level 2 (Cost: 2 `Attribute Points`)

    Roll to `Brace` or `Dodge` before the first attack

- Level 3 (Cost: 3 `Attribute Points`)

    Begin every defensive encounter by temporarily healing one creature for 30% HP.  When the encounter is over, the creature loses the temporary HP.

## **Tailwind**

`Tailwind` allows the player to roll twice for movement.  Only one roll may be used to move across the board; i.e., if a player rolls a 4 and then 8, they may choose to move 8 spaces, discarding the roll of 4.

- Level 1 (Cost: 2 `Attribute Points`)

## **Ascension**

`Ascension` swaps any two players' positions on the game board.  It can only be used once per charge; i.e., once a player uses `Ascension`, they must purchase another one using more `Attribute Points`.  Furthermore, the player receives `Astral Sickness` after casting, and cannot use `Ascension` on the next turn.

- Level 1 (Cost: 3 `Attribute Points` per charge)

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

