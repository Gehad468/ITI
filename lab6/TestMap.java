import java.util.*;

public class TestMap {
    private Map<Character, LinkedList<String>> wordsMap;

    public TestMap() {
        wordsMap = new HashMap<>();
        for (char c = 'a'; c <= 'z'; c++) {
            wordsMap.put(c, new LinkedList<>());
        }
        
        wordsMap.get('a').add("apple");
        wordsMap.get('b').add("banana");
        wordsMap.get('a').add("ant");
        wordsMap.get('b').add("ball");
        wordsMap.get('c').add("cat");
        wordsMap.get('d').add("dog");
        wordsMap.get('z').add("zebra");
    }

    public void printAllLettersAndWords() {
        for (Map.Entry<Character, LinkedList<String>> entry : wordsMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public void printWordsOfLetter(char letter) {
        LinkedList<String> words = wordsMap.get(Character.toLowerCase(letter));
        if (words != null) {
            System.out.println("Words starting with '" + Character.toLowerCase(letter) + "': " + words);
        } else {
            System.out.println("No words found for the letter '" + Character.toLowerCase(letter) + "'");
        }
    }

    public static void main(String[] args) {
        TestMap dictionary = new TestMap();
        
        dictionary.printAllLettersAndWords();
        
        System.out.println("\nPrinting words of letter 'a':");
        dictionary.printWordsOfLetter('a');
    }
}
