from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 10 

items = [
    {
        "id": 1,
        "title": "Dealing with Dragons",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1385526967i/150739.jpg",
        "author": "Patricia C. Wrede",
        "summary": "Meet Princess Cimorene--a princess who refuses to be proper. She is everything a princess is not supposed to be. Headstrong, tomobyish smart... And bored. So bored that she runs away to live with a dragon. And not just any dragon, but Kazul--one of the most powerful and dangerous dragons arounds. Of course, Cimorene has a way of hooking up with dangerous characters, and soon she's coping with a witch,a a jinn, a death-dealing talking bird, a stone prince, and some very oily wizards.",
        "score": "4.2",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Childrens", "Magic", "Adventure", "Humor"],
        "series": ["Dealing with Dragons", "Searching for Dragons", "Calling on Dragons", "Talking to Dragons"],
        "similar book ids": ["2", "3","5"],
    },
    {
        "id": 2,
        "title": "Searching for Dragons",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1593281257i/169875.jpg",
        "author": "Patricia C. Wrede",
        "summary": "Cimorene, the princess who refuses to be proper, is back--but where is Kazul the dragon? That's what Cimorene is determined to find out. Luckily--or perhaps not-so-luckily--she's got help: Mendenbar, the not-very-kingly King of the Enchanted Forest, has joined her in her quest. So with the aid of a broken-down magic carpet, a leaky magical sword, and a few buckets of soapy lemon water, they set off across the Enchanted Forest to tackle the dragon-napping and save the King of the Dragons.",
        "score": "4.27",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Childrens", "Magic", "Adventure", "Humor"],
        "series": ["Dealing with Dragons", "Searching for Dragons", "Calling on Dragons", "Talking to Dragons"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 3,
        "title": "Calling on Dragons",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1428442349i/169879.jpg",
        "author": "Patricia C. Wrede",
        "summary": "A Princess's work is never done--not even when she becomes a queen! Princess Cimorene is now Queen Cimorene ... and she's faced with her first queenly crisis -- the Enchanted Forest is threatened with complete destruction! Those wizards are back -- and they've become very smart. (Sort of.) They've figured out a way to take over the forest once and for all ... and what they have planned isn't pretty. With a little help from Kazul the dragon king, Morwen the witch, Telemain the magician, two cats, and a blue, flying donkey-rabbit named -- what else? -- Killer, Cimorene might just be able to stop them. And some people think that being a queen is easy.",
        "score": "4.18",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Childrens", "Magic", "Adventure", "Humor"],
        "series": ["Dealing with Dragons", "Searching for Dragons", "Calling on Dragons", "Talking to Dragons"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 4,
        "title": "Talking to Dragons",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1425951863i/169871.jpg",
        "author": "Patricia C. Wrede",
        "summary": "Always be polite to dragons! That's what Daystar's mother taught him...and it's a very wise lesson--one that might just help him after his mom hands him a magic sword and kicks him out of the house. Especially because his house sits on the edge of the Enchanted Forest and his mother is Queen Cimorene. But the tricky part is figuring out what he's supposed to do with the magic sword. Where is he supposed to go? And why does everyone he meets seem to know who he is? It's going to take a particularly hotheaded fire-witch, a very verbose lizard, and a badly behaved baby dragon to help him figure it all out. And those good manners certainly won't hurt!",
        "score": "4.19",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Childrens", "Magic", "Adventure", "Humor"],
        "series": ["Dealing with Dragons", "Searching for Dragons", "Calling on Dragons", "Talking to Dragons"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 5,
        "title": "Dragon Slippers",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1316730294i/669570.jpg",
        "author": "Jessica Day George",
        "summary": "Poor Creel. She can't believe her aunt wants to sacrifice her to the local dragon. It's a ploy to lure a heroic knight so that he will fight the dragon, marry Creel out of chivalrous obligation, and lift the entire family out of poverty. Creel isn't worried. After all, nobody has seen a dragon in centuries. But when the beast actually appears, Creel not only bargains with him for her life, she also ends up with a rare bit of treasure from his hoard, not gold or jewels, but a pair of simple blue slippers-or so she thinks. It's not until later that Creel learns a shocking truth: She possesses not just any pair of shoes, but ones that could be used to save her kingdom, which is on the verge of war, or destroy it.",
        "score": "4.25",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Fiction", "Magic", "Adventure", "Fairy Tales"],
        "series": ["Dragon Slippers", "Dragon Flight", "Dragon Spear"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 6,
        "title": "The Two Princesses of Bamarre",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1442734248i/183656.jpg",
        "author": "Gail Carson Levine",
        "summary": "Twelve-year-old Addie admires her older sister Meryl, who aspires to rid the kingdom of Bamarre of gryphons, specters, and ogres. Addie, on the other hand, is fearful even of spiders and depends on Meryl for courage and protection. Waving her sword Bloodbiter, the older girl declaims in the garden from the heroic epic of Drualt to a thrilled audience of Addie, their governess, and the young sorcerer Rhys. But when Meryl falls ill with the dreaded Gray Death, Addie must gather her courage and set off alone on a quest to find the cure and save her beloved sister. Addie takes the seven-league boots and magic spyglass left to her by her mother and the enchanted tablecloth and cloak given to her by Rhys - along with a shy declaration of his love. She prevails in encounters with tricky specters (spiders too) and outwits a wickedly personable dragon in adventures touched with romance and a bittersweet ending.",
        "score": "4.05",
        "genres": ["Fantasy", "Young Adult", "Dragons", "Fiction", "Middle Grade", "Fiction", "Fairy Tales", "Adventure", "Magic"],
        "series": ["The Lost Kingdom of Bamarre", "The Two Princesses of Bamarre"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 7,
        "title": "Alanna: The First Adventure",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388206270i/13831.jpg",
        "author": "Tamora Pierce",
        "summary": "From now on I'm Alan of Trebond, the younger twin. I'll be a knight. And so young Alanna of Trebond begins the journey to knighthood. Though a girl, Alanna has always craved the adventure and daring allowed only for boys; her twin brother, Thom, yearns to learn the art of magic. So one day they decide to switch places: Thom heads for the convent to learn magic; Alanna, pretending to be a boy, is on her way to the castle of King Roald to begin her training as a page.",
        "score": "4.27",
        "genres": ["Fantasy", "Young Adult", "Fiction", "Magic", "Adventure", "Middle Grade", "High Fantasy", "Childrens", "Teen"],
        "series": ["Alanna: The First Adventure", "In the Hand of the Goddess", "The Woman Who Rides Like a Man", "Lioness Rampant"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 8,
        "title": "Wild Magic",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1554192590i/13836.jpg",
        "author": "Tamora Pierce",
        "summary": "Young Daine's knack with horses gets her a job helping the royal horsemistress drive a herd of ponies to Tortall. Soon it becomes clear that Daine's talent, as much as she struggles to hide it, is downright magical. Horses and other animals not only obey, but listen to her words. Daine, though, will have to learn to trust humans before she can come to terms with her powers, her past, and herself.",
        "score": "4.31",
        "genres": ["Fantasy", "Young Adult", "Fiction", "Magic", "Adventure", "Middle Grade", "High Fantasy", "Childrens", "Teen"],
        "series": ["Wild Magic", "Wolf-Speaker", "Emperor Mage", "The Realms of the Gods"],
        "similar book ids": ["1", "3","5"],
    },

    {
        "id": 9,
        "title": "Wolf-Speaker",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1495451734i/24094.jpg",
        "author": "Tamora Pierce",
        "summary": "When humans start cutting down trees and digging holes in peaceful Dunlath Valley, the wolves know that something is wrong. They send a messenger to the only human who will listen -- Daine, a fourteen-year-old girl with the unpredictable power of wild magic. Daine and her closest companions heed the wolves' cry for help. But the challenge they are about to face in the valley is greater than they can possibly imagine.",
        "score": "4.21",
        "genres": ["Fantasy", "Young Adult", "Fiction", "Magic", "Adventure", "Middle Grade", "High Fantasy", "Childrens", "Teen"],
        "series": ["Wild Magic", "Wolf-Speaker", "Emperor Mage", "The Realms of the Gods"],
        "similar book ids": ["1", "3","5"],
    },

    
    {
        "id": 10,
        "title": "Fairest",
        "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348108149i/183660.jpg",
        "author": "Gail Carson Levine",
        "summary": "In the kingdom of Ayortha, who is the fairest of them all? Certainly not Aza. She is thoroughly convinced that she is ugly. What she may lack in looks, though, she makes up for with a kind heart, and with something no one else has-a magical voice. Her vocal talents captivate all who hear them, and in Ontio Castle they attract the attention of a handsome prince - and a dangerous new queen. In this masterful novel filled with humour, adventure, romance, and song, Newbery Honor author Gail Carson Levine invites you to join Aza as she discovers how exquisite she truly is.",
        "score": "3.89",
        "genres": ["Fantasy", "Young Adult", "Fiction", "Magic", "Adventure", "Middle Grade", "High Fantasy", "Childrens", "Teen"],
        "series": ["Ogre Enchanted", "Ella Enchanted", "Fairest"],
        "similar book ids": ["1", "3","5"],
    }

]


# ROUTES
@app.route('/popular_items')
def popular_items():
    global items
    return jsonify(items)

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('q', '')  # Get the search term from the query string
    # Fetch all items from your database
    # For this example, let's use a mock list of items
    global items
    # Filter the items to only include those where the title contains the search term
    matching_items = [item for item in items if search_term.lower() in item['title'].lower() or any(search_term.lower() 
    in genre.lower() for genre in item.get('genres', [])) or any(search_term.lower() in series.lower() for series in item.get('series', []))]


    # Return the matching items and the list of matches in JSON format
    return render_template('search_results.html', search_term=search_term, items=matching_items)
    

@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/view/<id>', methods=['GET'])
def view(id):
    # Fetch the item with the given id from your database
    global items
    item = items[int(id) - 1]   

    return render_template('view_item.html', item=item)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    # Fetch the item with the given id from your database
    global items
    item = items[int(id) - 1]   

    return render_template('edit_item.html', item=item)

@app.route('/edit_items', methods=['GET', 'POST'])
def edit_items():
    global items
    json_data = request.get_json()

    id_num = json_data["id"]
    id = int(id_num) - 1

    items[id]['title'] = json_data["title"] # update the title of the item with the given id
    items[id]['image'] = json_data["image"] # update the title of the item with the given id
    items[id]['author'] = json_data["author"] # update the title of the item with the given id
    items[id]['summary'] = json_data["summary"] # update the title of the item with the given id
    items[id]['score'] = json_data["score"] # update the title of the item with the given id
    items[id]['score'] = json_data["score"] # update the title of the item with the given id
    items[id]['genres'] = json_data["genres"].split(',') # update the title of the item with the given id
    items[id]['series'] = json_data["series"].split(',') # update the title of the item with the given id

    return jsonify(items=items)



@app.route('/add', methods=['GET', 'POST'])
def add_page():
    return render_template('add.html')



@app.route('/add_items', methods=['GET', 'POST'])
def add_items():
    global items 
    global current_id 

    json_data = request.get_json()   
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    genres_string = json_data["genres"]
    genres_list = genres_string.split(',')
    series_string = json_data["series"]
    series_list = series_string.split(',')

    new_item_entry = {
        "id": new_id,
        "title": json_data["title"],
        "image": json_data["image"],
        "author": json_data["author"],
        "summary": json_data["summary"],
        "score": json_data["score"],
        "genres": genres_list,
        "series": series_list
    }

    items.append(new_item_entry)

    return jsonify(items=items, new_id=new_id)




if __name__ == '__main__':
   app.run(debug = True)




