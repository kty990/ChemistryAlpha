const Profile = {
    relationshipTypes: {
        0: 'Short Term',
        1: 'Short Term Open To Long',
        2: 'Long Term Open To Short',
        3: 'Long Term'
    },

    // Variables
    name: '',
    age: 0,
    photos: [],
    bio: null,
    interests: [],
    relationshipType: this.relationshipTypes[2],

    // Functions
    new(name, age, photos = [], bio = null, interests = [], relationshipType = this.relationshipTypes[2]) {
        this.name = name;
        this.age = age;
        this.photos = photos;
        this.bio = bio;
        this.interests = interests;
        this.relationshipType = relationshipType;
    },

    edit(key, value) {
        this[key] = value;
    },

    delete() {
        // Send message to server to remove from db
    }
}