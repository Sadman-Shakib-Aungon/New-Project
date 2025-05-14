class MealPlan {
  constructor(userId, name, description) {
    this.id = generateUniqueId();
    this.userId = userId;
    this.name = name;
    this.description = description;
    this.meals = [];
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }
  
  addMeal(meal) {
    this.meals.push(meal);
    this.updatedAt = new Date();
  }
}