import datetime as dt
import pandas as pd
import hvplot.pandas
import holoviews as hv
import panel as pn

pn.extension()


ts_df = pd.read_csv('ts.csv', parse_dates=['timestamp'])
ts2_df = pd.read_csv('4weeks.csv', parse_dates=['timestamp'])


def spotify_player():
    spotify_embed = """<iframe src="https://open.spotify.com/embed/playlist/0tDd2EksvRLnC7bDBZvqgu?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    spotify_pane= pn.pane.HTML(spotify_embed)
    title = '''### Final Project--Audrey Bishop

    Use the Spotify player to listen to music as you scroll through my project.'''
    title_pane=pn.pane.Markdown(title, width=400)

    return pn.Row(title_pane, spotify_pane)


def fearless_music_videos(song_selection):
    if song_selection == 'Fearless':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/7lLigiVgJsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/46h1bAyKfsk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Fifteen':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/rLCol1C3ouc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/WDX4084bI78" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Love Story':
        video_embed1 ='''<iframe width="560" height="315" src="https://www.youtube.com/embed/aXzVF3XeS8M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 ='''<iframe width="560" height="315" src="https://www.youtube.com/embed/DBZpxr4xBbg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'You Belong With Me':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/vwp8Ur6tO-8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/a5viULNvdHI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Hey Stephen':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/tMhiHrL7rPE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/QHgFBeyoYJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'White Horse':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/9-rKvhsjwKU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/5CJxIs7RmuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Breathe':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/qsUK-BG5OQQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/zG11rkZ7c_c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Tell Me Why':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/cwFbq-70EwE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 =''' <iframe width="560" height="315" src="https://www.youtube.com/embed/nZ1MvFwTPAU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'You\'re Not Sorry':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/DNaSlUYIXBg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 ='''<iframe width="560" height="315" src="https://www.youtube.com/embed/uPdxiClFH7w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'The Way I Loved You':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/DlexmDDSDZ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2= '''<iframe width="560" height="315" src="https://www.youtube.com/embed/X31Z2N513L0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Forever & Always':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/T-41vMWQTUA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/wrtFtYuHtWU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'The Best Day':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/KZeI9I875Ig" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2='''<iframe width="560" height="315" src="https://www.youtube.com/embed/7banxRJy1uI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Change':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/jwWR1cQTKyw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/G2UpvUQ5X04" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Jump Then Fall':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/vUHDR6Rg3Y4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2= '''<iframe width="560" height="315" src="https://www.youtube.com/embed/KEZTkzSKnJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Untouchable':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/8bNlGwnEUAs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/yCyerNjAXP0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Forever & Always (Piano Version)':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/RcGowZ26sE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/GiTbNMC4lUI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Come In With the Rain':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/ePjcjLRHPOo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/Etp4i3I7Iyk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'SuperStar':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/IsCik8wznlU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 ='''<iframe width="560" height="315" src="https://www.youtube.com/embed/m2dMSsd1Ku8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'The Other Side of the Door':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/425n1NoRtgA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/ySAqzVDt4S0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''

    pane1 = pn.pane.HTML(video_embed1)
    pane2 = pn.pane.HTML(video_embed2)
    return  pn.Row(pane2, pane1)


def red_music_videos(song_selection):
    if song_selection == 'State of Grace':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/-mrC5tRkxrY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/QQsgJJ_CzBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Red':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/R_rUYuFtNO4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/Omk-8WxAHkI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Treacherous':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/u1D1AgDfreg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/bnKe_mzIJxU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'I Knew You Were Trouble':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/TqAollrUJdA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/uhcRzkLnZh4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'All Too Well':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/9OQBDdNHmXo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/rWp92atlmsM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == '22':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/9boiT64sm0Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/wSFidmPOO20" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'I Almost Do':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/w1AV_35zVwU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/6sXYfbz2HGs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'We Are Never Ever Getting Back Together':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/zJFcr1KyFqE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/nYvSliYJ8Ac" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Stay Stay Stay':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/OhJ-S9Nrh7Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/9y3jSlTgw8g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'The Last Time':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/pCH4QrSx2Jg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/eE-L5KIrc30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Holy Ground':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/S4PuN-IWi2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/kmgiRXSKSk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Sad Beautiful Tragic':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/jQfB4Gahi3I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/mDOvHK9PqbU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'The Lucky One':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/4LtQxA_ooLk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/0OWIAxH0FBE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Everything Has Changed':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/eMcMbWl0fDk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/sNqImjEOKi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Starlight':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/lPvcwgEuKTg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/U9twJCpM-t0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    elif song_selection == 'Begin Again':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/dXNZaHuKWNA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/jUL0-XMuIF0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'The Moment I Knew':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/LmXn6BU16e0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/jd4wdgFGGZQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Come Back... Be Here':
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/hHWOAUjnmjQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
        video_embed2 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/ofOwuV1_nZA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'Girl at Home':
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/CYZwvMFBa_Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed1 = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/UNckfN9upqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> '''
    elif song_selection == 'State of Grace (Acoustic Version)':
        video_embed1 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/D3mJe28un4M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
        video_embed2 = ''' <iframe width="560" height="315" src="https://www.youtube.com/embed/U_Nn8XBNIbQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''

    pane1 = pn.pane.HTML(video_embed1)
    pane2 = pn.pane.HTML(video_embed2)
    return  pn.Row(pane2, pane1)
