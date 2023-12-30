'''
_______________________________________________________________________________
_______________________________________________________________________________
File:       funksies.py  
Developer:  Ruimteman
Date:       12/08/2023
Description:
    Al die variebles wat ek nodig het om Who Wants to Be a Millionaire te speel    
_______________________________________________________________________________
_______________________________________________________________________________
'''

vrae_lys = [
  {
    "question": "Who wrote the play 'Hamlet'?",
    "options": [
      "William Shakespeare",
      "Charles Dickens",
      "Jane Austen",
      "F. Scott Fitzgerald"
    ],
    "answer": "William Shakespeare",
    "phone me": [
      "Hey, I'm pretty sure the author of 'Hamlet' is William Shakespeare.",
      "Uh, I think it might be Charles Dickens, but I'm not entirely sure.",
      "I'm leaning towards William Shakespeare as the writer of 'Hamlet'.",
      "Oh, I know this! The author of 'Hamlet' is... umm... Jane Austen!"
    ]
  },
  {
    "question": "What is the chemical symbol for gold?",
    "options": [
      "Go",
      "Au",
      "Ag",
      "Ge"
    ],
    "answer": "Au",
    "phone me": [
      "Hey, I'm pretty sure the chemical symbol for gold is Au.",
      "Uh, I think it might be Go, but I'm not entirely sure.",
      "I'm leaning towards Au as the symbol for gold.",
      "Oh, I know this! The symbol for gold is... umm... Ag!"
    ]
  },
  {
    "question": "Which planet is known as the 'Morning Star' or the 'Evening Star'?",
    "options": [
      "Mercury",
      "Venus",
      "Mars",
      "Saturn"
    ],
    "answer": "Venus",
    "phone me": [
      "Hey, I'm pretty sure the planet known as the 'Morning Star' or the 'Evening Star' is Venus.",
      "Uh, I think it might be Mercury, but I'm not entirely sure.",
      "I'm leaning towards Venus as the correct planet.",
      "Oh, I know this! The planet is... umm... Mars!"
    ]
  },
  {
    "question": "Who is the author of the book '1984'?",
    "options": [
      "George Orwell",
      "Aldous Huxley",
      "Ray Bradbury",
      "J.K. Rowling"
    ],
    "answer": "George Orwell",
    "phone me": [
      "Hey, I'm pretty sure the author of the book '1984' is George Orwell.",
      "Uh, I think it might be Aldous Huxley, but I'm not entirely sure.",
      "I'm leaning towards George Orwell as the author of '1984'.",
      "Oh, I know this! The author is... umm... Ray Bradbury!"
    ]
  },
  {
    "question": "What is the chemical formula for water?",
    "options": [
      "H2O",
      "CO2",
      "O2",
      "CH4"
    ],
    "answer": "H2O",
    "phone me": [
      "Hey, I'm pretty sure the chemical formula for water is H2O.",
      "Uh, I think it might be CO2, but I'm not entirely sure.",
      "I'm leaning towards H2O as the formula for water.",
      "Oh, I know this! The formula is... umm... O2!"
    ]
  },
  {
    "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
    "options": [
      "Amelia Earhart",
      "Bessie Coleman",
      "Harriet Quimby",
      "Jacqueline Cochran"
    ],
    "answer": "Amelia Earhart",
    "phone me": [
      "Hey, I'm pretty sure the first woman to fly solo across the Atlantic Ocean is Amelia Earhart.",
      "Uh, I think it might be Bessie Coleman, but I'm not entirely sure.",
      "I'm leaning towards Amelia Earhart for this achievement.",
      "Oh, I know this! The first woman to do this is... umm... Jacqueline Cochran!"
    ]
  },
  {
    "question": "What is the largest planet in our solar system?",
    "options": [
      "Venus",
      "Mars",
      "Jupiter",
      "Saturn"
    ],
    "answer": "Jupiter",
    "phone me": [
      "Hey, I'm pretty sure the largest planet in our solar system is Jupiter.",
      "Uh, I think it might be Venus, but I'm not entirely sure.",
      "I'm leaning towards Jupiter as the largest planet.",
      "Oh, I know this! The largest planet is... umm... Saturn!"
    ]
  },
  {
    "question": "Which historical figure is known for his theory of evolution by natural selection?",
    "options": [
      "Charles Darwin",
      "Isaac Newton",
      "Galileo Galilei",
      "Albert Einstein"
    ],
    "answer": "Charles Darwin",
    "phone me": [
      "Hey, I'm pretty sure the historical figure known for the theory of evolution by natural selection is Charles Darwin.",
      "Uh, I think it might be Isaac Newton, but I'm not entirely sure.",
      "I'm leaning towards Charles Darwin for the theory of evolution.",
      "Oh, I know this! The historical figure behind the theory of evolution is... umm... Galileo Galilei!"
    ]
  },
  {
    "question": "Which famous playwright wrote 'Romeo and Juliet'?",
    "options": [
      "William Shakespeare",
      "Jane Austen",
      "George Orwell",
      "Mark Twain"
    ],
    "answer": "William Shakespeare",
    "phone me": [
      "Hey, I'm pretty sure the famous playwright who wrote 'Romeo and Juliet' is William Shakespeare.",
      "Uh, I think it might be Jane Austen, but I'm not entirely sure.",
      "I'm leaning towards William Shakespeare for 'Romeo and Juliet'.",
      "Oh, I know this! The playwright behind 'Romeo and Juliet' is... umm... George Orwell!"
    ]
  },
  {
    "question": "Which gas do plants primarily use for photosynthesis?",
    "options": [
      "Oxygen",
      "Carbon Dioxide",
      "Nitrogen",
      "Hydrogen"
    ],
    "answer": "Carbon Dioxide",
    "phone me": [
      "Hey, I'm pretty sure plants primarily use Carbon Dioxide for photosynthesis.",
      "Uh, I think it might be Oxygen, but I'm not entirely sure.",
      "I'm leaning towards Carbon Dioxide for photosynthesis.",
      "Oh, I know this! The gas plants use for photosynthesis is... umm... Nitrogen!"
    ]
  },
  {
    "question": "Which famous scientist developed the theory of relativity?",
    "options": [
      "Isaac Newton",
      "Albert Einstein",
      "Galileo Galilei",
      "Stephen Hawking"
    ],
    "answer": "Albert Einstein",
    "phone me": [
      "Hey, I'm pretty sure the scientist who developed the theory of relativity is Albert Einstein.",
      "Uh, I think it might be Isaac Newton, but I'm not entirely sure.",
      "I'm leaning towards Albert Einstein as the one who developed the theory of relativity.",
      "Oh, I know this! The scientist behind the theory of relativity is... umm... Galileo Galilei!"
    ]
  },
  {
    "question": "Which ocean is the largest and deepest on Earth?",
    "options": [
      "Atlantic Ocean",
      "Indian Ocean",
      "Arctic Ocean",
      "Pacific Ocean"
    ],
    "answer": "Pacific Ocean",
    "phone me": [
      "Hey, I'm pretty sure the largest and deepest ocean on Earth is the Pacific Ocean.",
      "Uh, I think it might be the Atlantic Ocean, but I'm not entirely sure.",
      "I'm leaning towards the Pacific Ocean as the largest and deepest.",
      "Oh, I know this! The ocean that fits this description is... umm... the Indian Ocean!"
    ]
  },
  {
    "question": "Which famous painter is known for his 'Starry Night' and 'Sunflowers' paintings?",
    "options": [
      "Leonardo da Vinci",
      "Vincent van Gogh",
      "Pablo Picasso",
      "Michelangelo"
    ],
    "answer": "Vincent van Gogh",
    "phone me": [
      "Hey, I'm pretty sure the famous painter known for 'Starry Night' and 'Sunflowers' paintings is Vincent van Gogh.",
      "Uh, I think it might be Leonardo da Vinci, but I'm not entirely sure.",
      "I'm leaning towards Vincent van Gogh for these paintings.",
      "Oh, I know this! The painter behind these works is... umm... Pablo Picasso!"
    ]
  },
  {
    "question": "Which gas is responsible for the Earth's ozone layer depletion?",
    "options": [
      "Oxygen",
      "Carbon Dioxide",
      "Chlorofluorocarbons (CFCs)",
      "Methane"
    ],
    "answer": "Chlorofluorocarbons (CFCs)",
    "phone me": [
      "Hey, I'm pretty sure Chlorofluorocarbons (CFCs) are responsible for the Earth's ozone layer depletion.",
      "Uh, I think it might be Oxygen, but I'm not entirely sure.",
      "I'm leaning towards Chlorofluorocarbons (CFCs) for ozone layer depletion.",
      "Oh, I know this! The gas responsible for this is... umm... Carbon Dioxide!"
    ]
  },
  {
    "question": "Which natural disaster is measured using the Richter scale?",
    "options": [
      "Hurricanes",
      "Tornadoes",
      "Earthquakes",
      "Volcanic Eruptions"
    ],
    "answer": "Earthquakes",
    "phone me": [
      "Hey, I'm pretty sure earthquakes are measured using the Richter scale.",
      "Uh, I think it might be hurricanes, but I'm not entirely sure.",
      "I'm leaning towards earthquakes being measured with the Richter scale.",
      "Oh, I know this! The natural disaster measured this way is... umm... volcanic eruptions!"
    ]
  },
]

hulpmiddel_lys = ["1. Phone a friend", "2. 50/50", "3. Audiance"]

millionaire_money = [
  "$0",
  "$100",
  "$200",
  "$300",
  "$500",
  "$1,000",
  "$2,000",
  "$4,000",
  "$8,000",
  "$16,000",
  "$32,000",
  "$64,000",
  "$125,000",
  "$250,000",
  "$500,000",
  "$1,000,000"
]