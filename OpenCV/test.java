
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.CharBuffer;
import java.nio.charset.StandardCharsets;

public class test {

    

    public static void main(String[] args) {
        byte[] bigEndianBytes = new byte[] { 0x48, 0x65, 0x6c, 0x6c, 0x6f }; // Example bytes in big-endian format
        ByteBuffer buffer = ByteBuffer.wrap(bigEndianBytes).order(ByteOrder.BIG_ENDIAN); // Create ByteBuffer from byte array in big-endian format
        CharBuffer charBuffer = StandardCharsets.UTF_8.decode(buffer); // Decode ByteBuffer as UTF-8 string
        String str = charBuffer.toString(); // Convert CharBuffer to String
        System.out.println(str); // Output: "Hello"
    }

    

}

    
