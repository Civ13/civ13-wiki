# Contributing to the Wiki

**You can check what pages need fixing/content on the [github Issues section](https://github.com/Civ13/civ13-wiki/issues).**

Since this wiki is hosted on *github pages* using static Jekyll pages, it works slighly different from a regularly hosted wiki.

However, don't worry! It is simpler than it seems. You do **not** need to download the code (altough you can if you want to edit it locally). Follow the steps below:

1) If you do not have one yet, register for a **Github Account** [here](https://github.com/join).

2) Fork the wiki by going to the main project page [here](https://github.com/Civ13/civ13-wiki) and pressing the *Fork* button on the top right.

![image](assets/images/fork.PNG)

3) Go to your fork of the wiki (will be something like **YOURUSERNAME**.github.com/civ13-wiki), open settings, and scroll down to **GitHub Pages**. Make sure it looks similar to the screenshot below by activating Github Pages:

![image](assets/images/github_pages.PNG)

4) Your fork of the wiki is now live! You can now open the wiki using the link shown there. It will look similar to https://**YOURUSERNAME**.github.io/civ13-wiki

5) You're all set! Just edit by either creating a new page, or selecting **edit** on the top right menu, like the image below:

![image](assets/images/edit_menu.PNG)

6) The wiki pages are written in markdown and have the **.md** extension. They are located in the **wiki/** folder. If you add any images, put them in **assets/images/**. You can also use HTML on the pages if you need to, but its the best practice to keep to markdown unless its something you need html for (i.e., sortable tables).

7) When you feel that your changes are good enough, just open a pull request to the main repository (the one you forked), and if accepted, it will be displayed on the page! To open a pull request, 

8) Make sure you regularly update your repository to keep it up to date! You can do this using pull requests from master. Open your fork page on github and click **Pull Request** as per the image below:

![image](assets/images/pull_request.png)

## Images

While you can link external images using either markdown or html tags, we recommend that you upload them to **assets/images/** and link them from there. Make sure they have a unique name as to not replace current images!

## Downloading the code

If you prefer to edit the files locally, and/or want to experiment with the website layout, follow the steps below:

1) If you haven't, follow the steps **1** and **2** on the list above.

2) Using your preferred git client, download your fork (If you have no idea of what I'm talking about, use [GitHub Desktop](https://desktop.github.com/)).

3) You will need **Ruby** and **Jekyll** installed. If you do not have it yet, follow Jekyll's guide [here](https://jekyllrb.com/docs/installation/#guides).

4) Open the command line on whatever operating system you are using (***Terminal*** on Linux and MacOS, ***cmd*** or ***PowerShell*** on Windows), navigate to the civ13-wiki/ folder and run `bundle install` to update all the Ruby requirements.

5) You can now compile and run your local build! Run `bundle exec jekyll serve` and wait for it to compile. Then you can view the website by opening your browser and navigating to [http://localhost:4000](http://localhost:4000).

## Features 

* Improvements in the **cooperative** aspect: forks, pull-requests and roles.
* You can **customize your wiki** as you want with style sheets and even changing the layout. (see customization section below) 
* **No databases!** Only static files that can be downloaded in a few seconds.
* **Blazing fast** and free thankfully to Github/Gitlab Pages and Jekyll Server Side Generation process!
* **Markdown and html** mixed together!
* **Multiple free search engines!** on a static site!
* **History, revision comparison** and everything you need from a wiki platform.
* You can **edit your pages** with the standard git editor, prose.io (integrated) or any kind of editor you prefer.
* Non-existent wiki page links are "[red](red.md)", you can **click on them to automatically create a new page**!
* External links get the right icon automatically.
* **Component system with hooks** that allows you to totally customize your wiki UI. ([see customization documentation here](http://www.drassil.org/git-wiki/customize)) 
* Some **nice internal themes** to change your entire wiki UI with 1 simple configuration. ([see customization documentation here](http://www.drassil.org/git-wiki/customize))
* Automatic generated **TOC**
* You can download the entire wiki for **offline** usage and even navigate directly using a markdown reader.

Instructions and full documentation: http://drassil.github.io/git-wiki
