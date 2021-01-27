from greet import __version__


def test_version():
    assert __version__ == '0.1.0'


from greet.location import greet

def test_greet():
    result = greet("America/New_York")
    assert "New York!" in result


from greet.location import cli


def test_greet_cli(capsys):
    args = ["America/Argentina/San_Juan"]
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "San Juan!" in result

#this version is redudant, but part of the tutorial. It does not seem to work
#We discussed this in office hours, Here is the note as requested

#import subprocess

#def test_greet_cli2():
#    result = subprocess.run(["greet", "America/Costa_Rica"], capture_output=True)
#    assert b"Costa Rica!" in result.stdout
