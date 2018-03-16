#! /usr/bin/perl
use strict;
use warnings;
use utf8;
use v5.20.2;
use Data::Dump qw/dump/;
use File::Slurper qw/read_text/;
use Getopt::Long;
use autodie qw(:all);
use Log::Any qw($log);
use Log::Dispatch;
use Log::Any::Adapter;
use HTML::TreeBuilder;

binmode(STDOUT, ':utf8');

sub init_logging {
    # Send all logs to Log::Dispatch
    my $dispatch_logger = Log::Dispatch->new(
        outputs => [
            [ 'Screen', min_level => 'debug', newline => 1 ],
        ],
    );
    Log::Any::Adapter->set('Dispatch', dispatcher => $dispatch_logger);
}

init_logging();
$log->debugf("arguments are: %s", "foo");


my $data   = "file.dat";
my $length = 24;
my $verbose;

GetOptions ("length=i" => \$length,    # numeric
            "file=s"   => \$data,      # string
            "verbose"  => \$verbose)   # flag
    or die("Error in command line arguments\n");

sub main {
    for my $arg (@_) {
        my $content = read_text($arg);
        my $root = HTML::TreeBuilder->new_from_content($content);
        my $match = $root->look_down(class => 'entry-title');
        say "${arg}\t" . $match->as_text;
    }
}

main @ARGV;
