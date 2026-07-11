# Version 1
## Pokemon Center Queue Tracking
- URL for home page - https://www.pokemoncenter.com/en-gb
- when a new product releases, a virtual queue room will need to be entered and waited in to be able to access the site
- even if you are not interested in the new product and want to look at other products you still need to wait in the queue

### Research about Virtual Queue Room
- the URL does NOT seem to change, but this needs to be verified
- "No, the URL for the Pokémon Center UK does not change when the virtual queue is active. The site uses a shared redirect system. When your wait is over, you are automatically redirected to the main store while remaining on the same site domain" - Google AI, 2026

![Pokémon Center Queue](images/pcq1.png)

"Hi Trainer! You're in the virtual queue to access Pokemon Center!"

- from this screenshot we can see that the URL hasn't changed but there are keywords to look out for
- unfortunately, I will need to do my own test when there is a queue because I can't guarentee the queue will be the same every time
- but  if the bot looks for key words like "queue", "line", "wait" and etc, that may be my approach
- however it is hard not to notice that the "/en-gb" is removed from the URL when in the queue from other screenshots I have seen

### Things to Verify

- [ ] does the URL remain exactly the same?
- [ ] does the page title change?
- [ ] does the HTML structure change?
- [ ] is there a unique heading or element that Playwright can detect?
- [ ] does the queue provider expose a unique script or identifier?

### Possible approaches:

- detect keywords such as:
  - "queue"
  - "line"
  - "wait"
- detect a change in the page title
- detect a unique HTML element
- compare the DOM with the normal homepage