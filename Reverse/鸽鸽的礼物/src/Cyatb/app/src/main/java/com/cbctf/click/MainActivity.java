package com.cbctf.click;

import android.os.Bundle;
import android.media.MediaPlayer;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private MediaPlayer mediaPlayer;
    private List<Integer> audioList; // 音频资源列表
    private int currentIndex = 0; // 当前音频索引
    private int num = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        audioList = new ArrayList<>();
        audioList.add(R.raw.j);
        audioList.add(R.raw.n);
        audioList.add(R.raw.t);
        audioList.add(R.raw.m);
        TextView flag = findViewById(R.id.flag);
        Button Click = findViewById(R.id.click);
        Click.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                playNextAudio();
                num++;
                flag.setText(String.valueOf(num));
                if (num == 802){
                    flag.setText(decrypt("lrgm~;<lgk:j:hj:8594;<739<g6i3;37jh8g\u0080",  3));
                    playALL();
                }
            }
        });

    }
    private void playNextAudio() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }

        mediaPlayer = MediaPlayer.create(this, audioList.get(currentIndex));
        mediaPlayer.start();

        currentIndex = (currentIndex + 1) % audioList.size();
    }

    private void playALL() {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }

        mediaPlayer = MediaPlayer.create(this, R.raw.jntm);
        mediaPlayer.start();
        currentIndex = (currentIndex + 1) % audioList.size();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }

    public static String decrypt(String str, int key) {
        char[] charArray = str.toCharArray();
        StringBuilder sb1 = new StringBuilder();
        for (char c : charArray) {
            sb1.append((char) (c - key));
        }
        String sb2 = sb1.toString();
        StringBuilder plaintext = new StringBuilder();
        for (char word : sb2.toCharArray()) {
            if (Character.isUpperCase(word)) {
                plaintext.append((char) ((word - 'A' - key + 26) % 26 + 'A'));
            } else if (Character.isLowerCase(word)) {
                plaintext.append((char) ((word - 'a' - key + 26) % 26 + 'a'));
            } else {
                plaintext.append(word);
            }
        }
        return plaintext.toString();
    }

}