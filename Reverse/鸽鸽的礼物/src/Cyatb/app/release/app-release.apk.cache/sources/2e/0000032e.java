package f0;

import android.media.MediaPlayer;
import android.view.View;
import android.widget.TextView;
import com.cbctf.click.MainActivity;
import com.cbctf.click.R;

/* renamed from: f0.a  reason: case insensitive filesystem */
/* loaded from: classes.dex */
public final class View$OnClickListenerC0135a implements View.OnClickListener {

    /* renamed from: a  reason: collision with root package name */
    public final /* synthetic */ TextView f2147a;
    public final /* synthetic */ MainActivity b;

    public View$OnClickListenerC0135a(MainActivity mainActivity, TextView textView) {
        this.b = mainActivity;
        this.f2147a = textView;
    }

    @Override // android.view.View.OnClickListener
    public final void onClick(View view) {
        char[] charArray;
        MainActivity mainActivity = this.b;
        MediaPlayer mediaPlayer = mainActivity.f1559v;
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            mainActivity.f1559v.release();
        }
        MediaPlayer create = MediaPlayer.create(mainActivity, ((Integer) mainActivity.f1560w.get(mainActivity.f1561x)).intValue());
        mainActivity.f1559v = create;
        create.start();
        mainActivity.f1561x = (mainActivity.f1561x + 1) % mainActivity.f1560w.size();
        int i2 = mainActivity.f1562y + 1;
        mainActivity.f1562y = i2;
        String valueOf = String.valueOf(i2);
        TextView textView = this.f2147a;
        textView.setText(valueOf);
        if (mainActivity.f1562y == 802) {
            char[] charArray2 = "lrgm~;<lgk:j:hj:8594;<739<g6i3;37jh8g\u0080".toCharArray();
            StringBuilder sb = new StringBuilder();
            for (char c2 : charArray2) {
                sb.append((char) (c2 - 3));
            }
            String sb2 = sb.toString();
            StringBuilder sb3 = new StringBuilder();
            for (char c3 : sb2.toCharArray()) {
                if (Character.isUpperCase(c3)) {
                    sb3.append((char) (((c3 - '*') % 26) + 65));
                } else if (Character.isLowerCase(c3)) {
                    sb3.append((char) (((c3 - 'J') % 26) + 97));
                } else {
                    sb3.append(c3);
                }
            }
            textView.setText(sb3.toString());
            MediaPlayer mediaPlayer2 = mainActivity.f1559v;
            if (mediaPlayer2 != null) {
                mediaPlayer2.stop();
                mainActivity.f1559v.release();
            }
            MediaPlayer create2 = MediaPlayer.create(mainActivity, (int) R.raw.jntm);
            mainActivity.f1559v = create2;
            create2.start();
            mainActivity.f1561x = (mainActivity.f1561x + 1) % mainActivity.f1560w.size();
        }
    }
}