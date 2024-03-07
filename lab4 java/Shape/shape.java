import java.util.List;
abstract class MainShapes {
    public abstract void draw();
}

class circle extends MainShapes {
    @Override
    public void draw() {
        System.out.println("draw circle");
    }
}

class rect extends MainShapes {
    @Override
    public void draw() {
        System.out.println("draw rectangle");
    }
}
class TestClass {
    public void drawTest(List<? extends MainShapes> shapeList) {
        for (MainShapes shape : shapeList) {
            shape.draw();
        }
    }

}

public class shape {
    public static void main(String[] args) {
        TestClass test = new TestClass();

        List<circle> cirList = List.of(new circle());
        List<rect> recList = List.of(new rect());
        test.drawTest(cirList);
        test.drawTest(recList);
        test.drawTest(cirList);
        test.drawTest(recList);
    }
}