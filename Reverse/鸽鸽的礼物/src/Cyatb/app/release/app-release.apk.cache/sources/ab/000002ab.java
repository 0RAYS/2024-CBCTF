package com.cbctf.click;

import I.H;
import I.T;
import N0.c;
import android.content.res.Resources;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;
import androidx.activity.A;
import androidx.activity.l;
import androidx.activity.z;
import e.AbstractActivityC0131g;
import f0.View$OnClickListenerC0135a;
import java.util.ArrayList;
import java.util.WeakHashMap;

/* loaded from: classes.dex */
public class MainActivity extends AbstractActivityC0131g {

    /* renamed from: z  reason: collision with root package name */
    public static final /* synthetic */ int f1558z = 0;

    /* renamed from: v  reason: collision with root package name */
    public MediaPlayer f1559v;

    /* renamed from: w  reason: collision with root package name */
    public ArrayList f1560w;

    /* renamed from: x  reason: collision with root package name */
    public int f1561x = 0;

    /* renamed from: y  reason: collision with root package name */
    public int f1562y = 0;

    /* JADX WARN: Multi-variable type inference failed */
    /* JADX WARN: Type inference failed for: r0v10, types: [androidx.activity.p] */
    /* JADX WARN: Type inference failed for: r0v11, types: [java.lang.Object, I.s] */
    @Override // e.AbstractActivityC0131g, androidx.activity.k, x.f, android.app.Activity
    public final void onCreate(Bundle bundle) {
        Object obj;
        super.onCreate(bundle);
        int i2 = l.f807a;
        z zVar = z.f827a;
        A a2 = new A(0, 0, zVar);
        A a3 = new A(l.f807a, l.b, zVar);
        View decorView = getWindow().getDecorView();
        c.d(decorView, "window.decorView");
        Resources resources = decorView.getResources();
        c.d(resources, "view.resources");
        boolean booleanValue = ((Boolean) zVar.b(resources)).booleanValue();
        Resources resources2 = decorView.getResources();
        c.d(resources2, "view.resources");
        boolean booleanValue2 = ((Boolean) zVar.b(resources2)).booleanValue();
        int i3 = Build.VERSION.SDK_INT;
        if (i3 >= 29) {
            obj = new Object();
        } else if (i3 >= 26) {
            obj = new Object();
        } else {
            obj = new Object();
        }
        ?? r02 = obj;
        Window window = getWindow();
        c.d(window, "window");
        r02.a(a2, a3, window, decorView, booleanValue, booleanValue2);
        setContentView(R.layout.activity_main);
        View findViewById = findViewById(R.id.main);
        ?? obj2 = new Object();
        WeakHashMap weakHashMap = T.f314a;
        H.u(findViewById, obj2);
        ArrayList arrayList = new ArrayList();
        this.f1560w = arrayList;
        arrayList.add(Integer.valueOf((int) R.raw.f3422j));
        this.f1560w.add(Integer.valueOf((int) R.raw.f3424n));
        this.f1560w.add(Integer.valueOf((int) R.raw.f3425t));
        this.f1560w.add(Integer.valueOf((int) R.raw.f3423m));
        ((Button) findViewById(R.id.click)).setOnClickListener(new View$OnClickListenerC0135a(this, (TextView) findViewById(R.id.flag)));
    }

    @Override // e.AbstractActivityC0131g, android.app.Activity
    public final void onDestroy() {
        super.onDestroy();
        MediaPlayer mediaPlayer = this.f1559v;
        if (mediaPlayer != null) {
            mediaPlayer.release();
            this.f1559v = null;
        }
    }
}