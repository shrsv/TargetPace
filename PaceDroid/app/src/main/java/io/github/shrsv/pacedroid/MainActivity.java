package io.github.shrsv.pacedroid;

import android.os.Bundle;
import android.os.Debug;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends ActionBarActivity  {

    public void calc(View v){
        double dist, reqd_pace;
        int tgt_time, m, s;

        EditText et_dist;
        EditText et_tgt_time;

        et_dist = (EditText) findViewById(R.id.editText);
        et_tgt_time = (EditText) findViewById(R.id.editText2);

        dist = Double.parseDouble(et_dist.getText().toString());
        tgt_time = Integer.parseInt(et_tgt_time.getText().toString()) * 60;

        reqd_pace = tgt_time/dist;

        m = (int) (reqd_pace/60);
        s = (int) reqd_pace - m * 60;

        Toast.makeText(this, String.format("Target this pace: %d:%d mins/km", m, s), Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
