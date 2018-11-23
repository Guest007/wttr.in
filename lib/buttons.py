TWITTER_BUTTON = """
<a href="https://twitter.com/igor_chubin" class="twitter-follow-button" data-show-count="false" data-button="grey">Follow @igor_chubin</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
"""

GITHUB_BUTTON = """
<!-- Place this tag where you want the button to render. -->
<a aria-label="Star chubin/wttr.in on GitHub" data-count-aria-label="# stargazers on GitHub" data-count-api="/repos/chubin/wttr.in#stargazers_count" data-count-href="/chubin/wttr.in/stargazers" data-icon="octicon-star" href="https://github.com/chubin/wttr.in" class="github-button">wttr.in</a>
"""

GITHUB_BUTTON_2 = """
<!-- Place this tag where you want the button to render. -->
<a aria-label="Star schachmat/wego on GitHub" data-count-aria-label="# stargazers on GitHub" data-count-api="/repos/schachmat/wego#stargazers_count" data-count-href="/schachmat/wego/stargazers" data-icon="octicon-star" href="https://github.com/schachmat/wego" class="github-button">wego</a>
"""

GITHUB_BUTTON_3 = """
<!-- Place this tag where you want the button to render. -->
<a aria-label="Star chubin/pyphoon on GitHub" data-count-aria-label="# stargazers on GitHub" data-count-api="/repos/chubin/pyphoon#stargazers_count" data-count-href="/chubin/pyphoon/stargazers" data-icon="octicon-star" href="https://github.com/chubin/pyphoon" class="github-button">pyphoon</a>
"""

GITHUB_BUTTON_FOOTER = """
<!-- Place this tag right after the last button or just before your close body tag. -->
<script async defer id="github-bjs" src="https://buttons.github.io/buttons.js"></script>
"""

def add_buttons(output):
    """
    Add buttons to html output
    """

    return output.replace('</body>',
                          (TWITTER_BUTTON
                           + GITHUB_BUTTON
                           + GITHUB_BUTTON_3
                           + GITHUB_BUTTON_2
                           + GITHUB_BUTTON_FOOTER) + '</body>')
