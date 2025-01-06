from app.models import db, Song
from sqlalchemy.sql import text
from datetime import datetime, date
from app.models.db import environment, SCHEMA


def seed_songs():
    song1 = Song(
            title = "One more time",
            artist = "Daft Punk",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 313,
            lyrics = """Strangers, from strangers into brothers
From brothers into strangers once again
We saw the whole world
But I couldn't see the meaning
I couldn't even recognize my friends
Older, but nothing's any different
Right now feels the same, I wonder why
I wish they told us
It shouldn't take a sickness
Or airplanes falling out the sky
Do I have to die to hear you miss me?
Do I have to die to hear you say goodbye?
I don't wanna act like there's tomorrow
I don't wanna wait to do this one more time
One more time
One more
One more time
One more time
I miss you, took time but I admit it
It still hurts even after all these years
And I know that next time, ain't always gonna happen
I gotta say, "I love you" while we're here
Do I have to die to hear you miss me?
Do I have to die to hear you say goodbye?
I don't wanna act like there's tomorrow
I don't wanna wait to do this one more time
One more time
One more
One more time
One more time
One more time
One more time
One more
One more time
One more time
One more time
I miss you""",
            audio_file = "https://melody-songs.s3.us-east-1.amazonaws.com/07a9740ea7754e2292a349e8d6932620.mp3"
            )
    song2 = Song(
            title = "Harder, Better, Faster, Stronger",
            artist = "Daft Punk",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 224,
            lyrics = """Work it, make it
Do it, makes us
Harder, better
Faster, stronger
More than, hour
Hour, never
Ever, after
Work is, over
Work it, make it
Do it, makes us
Harder, better
Faster, stronger
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
Work it harder, make it
Do it faster, makes us
More than ever, hour after hour
Work is never over
Work it harder, make it better
Do it faster, makes us strong
More than ever, hour after hour
Work is never over
Work it, make it better
Do it faster makes us stronger
More than ever, hour after hour
Work is never over
Work it, make it better
Do it faster makes us stronger
More than ever, hour after hour
Work is never over
Work it, make it better
Do it faster makes us stronger
More than ever, hour after hour
Work is never over
Work it harder
Do it faster
More than ever, hour
Work is never over
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over""",
            audio_file = "https://melody-songs.s3.amazonaws.com/02c817bb7d974bb8a7f25dcfac60d0ef.mp3"
            )
    song3 = Song(
            title = "Veridis Quo",
            artist = "Daft Punk",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 344,
            lyrics = """darararar rururrrr""",
            audio_file = "https://melody-songs.s3.amazonaws.com/51b3aecc46d5413eb57d7d95c44bf0ab.mp3"
            )
    song4 = Song(
            title = "Controlla",
            artist = "Drake",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 2,
            user_id = 1,
            duration = 245,
            lyrics = """Right, my yiy just changed
You just buzzed the front gate
I thank God you came
How many more days could I wait?
I made plans with you
And I won't let 'em fall through
I, I, I, I, I
I think I'd lie for you
I think I'd die for you
Jodeci "Cry For You"
Do things when you want me to
Like controlla, controlla, yeah
Like controlla, controlla, yeah
Okay, you like it
When I get, aggressive, tell you to
Go slower, go faster
Like controlla, controlla, yeah
Like controlla, controlla, yeah
And I'm never on a waste ting, shorty
I do it how you say you want it
Them girls, they just wanna take my money
They don't want me to give you nothing
They don't want you to have nothing
They don't wanna see me find your lovin'
They don't wanna see me
Smiling back when they pree
Knowing I'd lie for you
Thinking I'd die for you
Jodeci "Cry For You"
Do things when you want me to
Like controlla, controlla, yeah
Like controlla, controlla, yeah
Gyal a tear off mi garments
And a bawl fi come inna mi apartment, woi
Di gyal dem want di length and strength
Action speak louder than argument well
But you can't just diss and come tell man "sorry"
You can't listen to me talk and go tell my story, nah
It don't work like that when you love somebody
My old flex is my new flex now and we're workin' on it, yeah
And that's why I need all the energy that you bring to me
My last girl would tear me apart, but she'd never wanna split a ting with me
But when it comes to you, you
I think I'd lie for you
I think I'd die for you
Do things when you want me to
Like controlla, controlla, yeah
Like controlla, controlla, yeah
And I'm never on a waste ting, shorty
I do it how you say you want it
Them girls, they just wanna take my money
They don't want me to give you nothing
They don't want you to have nothing
They don't wanna see me find your lovin'
They don't wanna see me
Smiling back when they pree
Jeez!
Music a drop
Gyal a whine up dem bumpa
Dis is di summa summa controlla alert
Drake from Canada, Beenie Man from Jamaica
Dah one yah a murda
Zaga""",
            audio_file = "https://melody-songs.s3.amazonaws.com/8b461a8a1ece4b7baf48cc9de8502980.mp3"
            )
    song5 = Song(
            title = "One Dance",
            artist = "Daft Punk",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 2,
            user_id = 1,
            duration = 174,
            lyrics = """Baby, I like your style
Grips on your waist
Front way, back way
You know that I don't play
Streets not safe
But I never run away
Even when I'm away
OT, OT, there's never much love when we go OT
I pray to make it back in one piece
I pray, I pray
That's why I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me
I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me
Baby, I like your style
Strength and guidance
All that I'm wishin' for my friends
Nobody makes it from my ends
I had to bust up the silence
You know you gotta stick by me
Soon as you see the text, reply me
I don't wanna spend time fighting
We've got no time
And that's why I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me
I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me
Got a pretty girl and she love me long time
Wine it, wine it, and she love me long time
Ooh yeah, just steady and wine up
Back up, back up, back up and wine up
Back up, back up and wine it
Girl, just back up, back up, back up and wine down
Ooh yeah, just steady and wine up
Back, up, back up and wine it, girl
Ooh, tell me
I need to know, where do you wanna go?
'Cause if you're down, I'll take it slow
Make you lose control
Where, where, where
Where, where, where, where (ooh yeah, very long time)
(Back, up, back up and wine it, girl)
'Cause if you're down (back up, back up and)
'Cause if you're down (back up, back up and)
'Cause if you're down (back up, back up and)
I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me
I need a one dance
Got a Hennessy in my hand
One more time 'fore I go
Higher powers taking a hold on me""",
            audio_file = "https://melody-songs.s3.amazonaws.com/cbb7b79f39b141a6b5c725766d24b7fc.mp3"
            )
    song6 = Song(
            title = "Too Good",
            artist = "Drake",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 2,
            user_id = 1,
            duration = 225,
            lyrics = """Oh yeah, yeah, yeah
Oh yeah, yeah, yeah
Yeah
Look... I don't know how to talk to you
I don't know how to ask you if you're okay
My friends always feel the need to tell me things
Seems like they're just happier than us these days
Yeah, these days I don't know how to talk to you
I don't know how to be there when you need me
It feels like the only time you see me
Is when you turn your head to the side and look at me differently
Yeah, and last night I think I lost my patience
Last night I got high as your expectations
Last night, I came to a realization
And I hope you can take it
I hope you can take it
I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
No, I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
I don't know how to talk to you
I just know I found myself getting lost with you
Lately you just make me work too hard for you
Got me on flights overseas, and I still can't get across to you
And last night I think I lost my patience
Last night I got high as your expectations
Last night, I came to a realization
And I hope you can take it
I hope you can take it
I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
No, I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
Years go by too fast
I can't keep track
How long did we last?
I feel bad for asking
It can't end like this
We gotta take time with this
Cock up yuh bumper, sit down pon it
Let me see if this is something I can fix
You got somebody other than me
Don't play the victim when you're with me
Free time is costing me more than it seems
Sacrificing things
And I wanna tell you my intentions
I wanna do the things that I mention
I wanna benefit from the friendship
I wanna get the late night message from you, from you
I put my hands around you
Gotta get a handle on you
Gotta get a handle on the fact that...
I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
No, I'm too good to you
I'm way too good to you
You take my love for granted
I just don't understand it
Gyal a you mi waan
Pay fi yuh visa meck yo fly out regular
Baby, cock up yuh bumper, sit down pon it
Gyal yo pum pum good and yuh fit
Mi wi give you everything weh deh in my wallet
And in my pocket
Cock up yuh bumper, sit down pon it
Gyal yo pum pum good and yuh fit
Mi wi give you everything weh deh in my wallet
And in my pocket""",
            audio_file = "https://melody-songs.s3.amazonaws.com/63a53b6b0f83464e8e2ca2225aabbd0a.mp3"
            )
    song7 = Song(
            title = "POWER",
            artist = "Kanye",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 3,
            user_id = 1,
            duration = 138,
            lyrics = """I'm living in that 21st century
Doing something mean to it
Do it better than anybody you ever seen do it
Screams from the haters, got a nice ring to it
I guess every superhero need his theme music
No one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the power
(21st-century schizoid man)
The system broken, and the school's closed, the prisons open
We ain't got nothin' to lose, motherfucker, we rollin'
Huh? Motherfucker, we rollin'
With some light-skinned girls and some Kelly Rowlands
In this white man's world, we the ones chosen
So goodnight, cruel world, I'll see you in the mornin'
Huh? I'll see you in the mornin'
This is way too much, I need a moment
No one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the power
'Til then, fuck that, the world's ours
And they say, and they say
And they say, and they say
And they say, and they say
(21st-century schizoid man)
Fuck SNL and the whole cast
Tell 'em Yeezy said they can kiss my whole ass
More specifically, they can kiss my asshole
I'm an asshole? You niggas got jokes
You short-minded niggas thoughts is Napoleon
My furs is Mongolian, my ice brought the goalies in
Now I embody every characteristic of the egotistic
He knows he so fuckin' gifted
I just needed time alone, with my own thoughts
Got treasures in my mind but couldn't open up my own vault
My childlike creativity, purity and honesty
Is honestly being crowded by these grown thoughts
Reality is catching up with me
Taking my inner child, I'm fighting for custody
With these responsibilities that they entrusted me
As I look down at my diamond encrusted piece
Thinkin', no one man should have all that power
The clock's ticking, I just count the hours
Stop tripping, I'm tripping off the powder
'Til then, fuck that, the world's ours
And they say, and they say
And they say, and they say
And they say, and they say
(21st-century schizoid man)
Colin Powells, Austin Powers
Lost in translation with a whole fuckin' nation
They say I was the abomination of Obama's nation
Well that's a pretty bad way to start the conversation
At the end of the day, goddammit, I'm killin' this shit
I know damn well y'all feeling this shit
I don't need your pussy, bitch, I'm on my own dick
I ain't gotta power trip, who you goin' home with?
How 'Ye doing? I'm surviving
I was drinking earlier, now I'm driving
Where the bad bitches, huh? Where y'all hiding?
I got the power make your life so exciting
Now this will be a beautiful death
I'm jumping out the window
I'm letting everything go
I'm letting everything go
Mmm, now this will be a beautiful death
I'm jumping out the window
I'm letting everything go
I'm letting everything go
Now this will be a beautiful death
Jumping out the window
Letting everything go
Letting everything go
You got the power to let power go?""",
            audio_file = "https://melody-songs.s3.amazonaws.com/fd1f16ba04be465797a791136a4d6568.mp3"
            )
    song8 = Song(
            title = "Runaway",
            artist = "Kanye",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 3,
            user_id = 1,
            duration = 548,
            lyrics = """Look at ya, look at ya, look at ya, look at ya
Look at ya, look at ya, look at ya, look at ya
Look at ya, look at ya, look at ya, look at ya
Look at ya, look at ya (ladies and gentlemen)
Look at ya, look at ya (ladies, ladies and gentlemen)
And I always find, yeah, I always find somethin' wrong
You been puttin' up wit' my shit just way too long
I'm so gifted at findin' what I don't like the most
So I think it's time (so I think it's time)
For us to have a toast
Let's have a toast for the douche bags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk offs
That'll never take work off
Baby, I got a plan
Run away fast as you can
She find pictures in my email
I sent this bitch a picture of my dick
I don't know what it is with females
But I'm not too good at that shit
See, I could have me a good girl
And still be addicted to them hood rats
And I just blame everything on you
At least you know that's what I'm good at
And I always find
Yeah, I always find
Yeah, I always find somethin' wrong
You been puttin' up wit' my shit just way too long
I'm so gifted at findin' what I don't like the most
So I think it's time (so I think it's time)
For us to have a toast
Let's have a toast for the douche bags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk offs
That'll never take work off
Baby, I got a plan
Run away fast as you can
Run away from me, baby
Run away
Run away from me, baby
Run away
When it starts to get crazy, then run away
Babe, I got a plan, run away as fast as you can
Run away from me, baby
Run away
Run away from me, baby
Run away
When it starts to get crazy
Why can't she just run away?
Baby, I got a plan
Run away as fast as you can
Twenty-four seven, three sixty-five
Pussy stays on my mind
I-I-I-I did it
Alright, alright, I admit it
Now pick your next move
You can leave or live wit' it
Ichabod Crane with that mothafuckin' top off
Split and go where?
Back to wearin' knockoffs? Haha
Knock it off, Neiman's, shop it off
Let's talk over mai tais, waitress, top it off
Hoes like vultures, wanna fly in your Freddy loafers
You can't blame 'em, they ain't never seen Versace sofas
Every bag, every blouse, every bracelet
Comes with a price tag, baby, face it
You should leave if you can't accept the basics
Plenty hoes in the baller-nigga matrix
Invisibly set, the Rolex is faceless
I'm just young, rich, and tasteless
P
Never was much of a romantic
I could never take the intimacy
And I know it did damage
'Cause the look in your eyes is killin' me
I guess then you at an advantage
'Cause you could blame me for everything
And I don't know how I'ma manage
If one day you just up and leave
And I always find, yeah, I always find somethin' wrong
You been puttin' up wit' my shit just way too long
I'm so gifted at findin' what I don't like the most
So I think it's time (so I think it's time)
For us to have a toast
Let's have a toast for the douche bags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk offs
That'll never take work off
Baby, I got a plan
Run away fast as you can""",
            audio_file = "https://melody-songs.s3.amazonaws.com/9df4fa70d6db4ae296be72632e952251.mp3"
            )
    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()
        