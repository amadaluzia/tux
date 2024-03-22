import discord
from discord import app_commands

from tux.command_cog import CommandCog
from tux.main import TuxBot
from tux.utils.tux_logger import TuxLogger

logger = TuxLogger(__name__)


des_ids = [
    [1175177565086953523, "_kde"],
    [1175177703066968114, "_gnome"],
    [1175177036990533795, "_i3"],
    [1175222139046080582, "_hyprland"],
    [1175177087183769660, "_sway"],
    [1175243354557128765, "_xfce"],
    [1175220317174632489, "_dwm"],
    [1175177142108160121, "_bspwm"],
    [1181288708977205318, "_cinnamon"],
    [1175242546012753941, "_xmonad"],
    [1175241189935550554, "_awesome"],
    [1175245686489501726, "_mate"],
    [1175241537689489408, "_qtile"],
    [1175221470587256852, "_emacs"],
    [1175240614124732487, "_herbstluft"],
    [1175219898113331331, "_icewm"],
    [1175337897180803082, "_openbox"],
    [1175336806963744788, "_wayfire"],
    [1185972642260455445, "_berry"],
    [1192097654818226256, "_leftwm"],
    [1192149690096033882, "_budgie"],
    [1196324646170148925, "_riverwm"],
    [1212033435858898995, "_enlightenment"],
    [1212031657805221930, "_stumpwm"],
]

distro_ids = [
    [1175176142899122246, "_arch"],
    [1175176866928263220, "_debian"],
    [1175176922460860517, "_fedora"],
    [1175176812293271652, "_ubuntu"],
    [1175235143707918436, "_windows"],
    [1175176279616663573, "_gentoo"],
    [1175227850119458897, "_freebsd"],
    [1175177831551086593, "_nixos"],
    [1175178088347344916, "_void"],
    [1175176981936087161, "_opensuse"],
    [1175244437530611712, "_macos"],
    [1175241975818092564, "_alpine"],
    [1175177993526726717, "_linuxmint"],
    [1175221054684286996, "_openbsd"],
    [1176533514385096714, "_bedrock"],
    [1178347402730688542, "_endeavouros"],
    [1178391378812735508, "_artix"],
    [1182152672447569972, "_slackware"],
    [1178347123905929316, "_popos"],
    [1175177750143848520, "_kisslinux"],
    [1180570700734546031, "tux"],
    [1191106506276479067, "_garuda"],
    [1192177499413684226, "_asahi"],
    [1207599112585740309, "_fedoraatomic"],
]

lang_ids = [
    [1175612831996055562, "_python"],
    [1175612831861837864, "_bash"],
    [1175612831941525574, "_html"],
    [1175612831115260006, "_javascript"],
    [1175612831652139008, "_c"],
    [1175612832029609994, "_cplusplus"],
    [1175612831790534797, "_lua"],
    [1175612831631155220, "_rust"],
    [1175612831907979336, "_java"],
    [1175612831798939648, "_csharp"],
    [1178389324098699294, "_php"],
    [1175612831798931556, "_haskell"],
    [1175612831727632404, "_ruby"],
    [1175612831828295680, "_kotlin"],
    [1175739620437266443, "_go"],
    [1175612831731822734, "_lisp"],
    [1175612831920558191, "_perl"],
    [1185975879231348838, "_asm"],
    [1175612830389633164, "_ocaml"],
    [1175612831727620127, "_erlang"],
    [1175612831287218250, "_zig"],
    [1175612831878615112, "_julia"],
    [1175612831429824572, "_crystal"],
    [1175612831761182720, "_elixir"],
    [1207600618542206976, "_clojure"],
]

vanity_ids = [
    [1179277471883993219, "wheel"],
    [1197348658052616254, "mag"],
    [1175237664811790366, "regional_indicator_e"],
    [1186473849294962728, "smirk_cat"],
    [1180568491527516180, "supertuxkart"],
    [1179551412070404146, "100"],
    [1183896066588950558, "rabbit"],
    [1192245668534833242, "cd"],
    [1179551519624925294, "hugging"],
    [1183897526613577818, "hdtroll"],
    [1175756229168079018, "_git"],
    [1197353868103782440, "goblin"],
    [1202544488262664262, "bar_chart"],
    [1186473904773017722, "man_mage"],
    [1208233484230074408, "ghost"],
    [1217601089721995264, "old_man"],
    [1217866697751400518, "ear_of_rice"],
    [1212039041269366854, "chess_pawn"],
]

misc_ids = [
    [1182069378636849162, "_vsc"],
    [1180571441276649613, "_nvim"],
    [1180660198428393643, "_emacs"],
    [1192140446919561247, "_gnunano"],
    [1193242175295729684, "_kate"],
    [1192135710443065345, "_micro"],
    [1193241331221405716, "_jetbrains"],
    [1185974067472380015, "_helix"],
    [1192139311919935518, "_kakoune"],
    [1187804435578093690, "_ed"],
    [1189236454153527367, "_gecko"],
    [1189236400571301958, "_chromium"],
]

# TODO: Figure out how to make this work without hard coding the roles and emojis.


class RoleCount(CommandCog):
    @app_commands.command(
        name="rolecount", description="Shows the number of users in each role."
    )
    @app_commands.describe(which="Which option to list!")
    @app_commands.choices(
        which=[
            app_commands.Choice(name="Distros", value="ds"),
            app_commands.Choice(name="Languages", value="lg"),
            app_commands.Choice(name="DE/WMs", value="de"),
            app_commands.Choice(name="Misc", value="misc"),
            app_commands.Choice(name="Vanity", value="vanity"),
        ]
    )
    async def role_count(
        self, interaction: discord.Interaction, which: discord.app_commands.Choice[str]
    ):
        data_embed: discord.Embed = discord.Embed(
            title=f"All Things Linux stats for {which.name}",
            color=discord.Color.random(),
            timestamp=interaction.created_at,
        )

        data_embed.set_footer(
            text=f"Requested by {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar,
        )

        if interaction.guild:
            match which.value:
                case "ds":  # Distros
                    roles_emojis = distro_ids

                case "lg":  # Languages
                    roles_emojis = lang_ids

                case "de":  # DE/WMs
                    roles_emojis = des_ids

                case "misc":  # Misc roles
                    roles_emojis = misc_ids

                case "vanity":  # Vanity roles
                    roles_emojis = vanity_ids

            for role_emoji in roles_emojis:
                role = interaction.guild.get_role(role_emoji[0])
                emoji = discord.utils.get(self.bot.emojis, name=role_emoji[1])

                if role and emoji:
                    data_embed.add_field(
                        name=f"{str(emoji)} {role.name}",
                        value=f"{len(role.members)} users",
                        inline=True,
                    )
                else:
                    missing = "Role" if role is None else "Emoji"
                    logger.warning(
                        f"Cannot find {missing} with ID {role_emoji[0]} or name {role_emoji[1]}"
                    )

        await interaction.response.send_message(embed=data_embed)
        logger.info(f"{interaction.user} requested role count for {which.name}.")


async def setup(bot: TuxBot) -> None:
    await bot.add_cog(RoleCount(bot))
