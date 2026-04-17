db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE || "blog_db");

db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "content", "author"],
      properties: {
        title: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        content: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        author: {
          bsonType: "string",
          description: "must be a string and is required"
        }
      }
    }
  }
});

db.posts.insertMany([
  {
    title: "Docker Compose",
    content: "Introduction a l'orchestration multi-services.",
    author: "Geoffrey"
  },
  {
    title: "MongoDB",
    content: "Base NoSQL orientee documents.",
    author: "Geoffrey"
  },
  {
    title: "MySQL",
    content: "Base relationnelle classique.",
    author: "Geoffrey"
  },
  {
    title: "FastAPI",
    content: "Framework Python rapide pour les API.",
    author: "Geoffrey"
  },
  {
    title: "Healthchecks",
    content: "Les tests doivent valider le contenu metier.",
    author: "Geoffrey"
  }
]);
